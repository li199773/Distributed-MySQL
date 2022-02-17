# `MySQL` + `Python`
## 01 `MySQL分区`:将数据分成几个表格，在数据库还是显示一个表格，不是真正的逻辑物理分表
### 1.分区的分类：
    1.求余算法
    key算法：内置的key算法运算数字
        partition by key(id) partitions 2;
    hash算法：内置的hash算法运算数字
        partition by hash(id) partitions 2;
    2.范围区间
    range:区间
        # 7天分一个区
        partition by range(num)
        (partition 1_7 values less than(8),
        partition 8_14 values less than(15));
    list:范围
        # 跟range类似
        partition by list(num)
        (partition 1_7 values in(1,2,3,4,5,6,7),
        partition 8_14 values in(8,9,10,11,12,13,14),
        partition 15_21 values in(15,16,17,18,19,20,21),
        partition 22_28 values in(22,23,24,25,26,27,28));
### 2.分区的修改和删除
    删除分区：
    1.求余分区的情况下不会删除数据，数据会自定分配给其他的分区
    2.范围分区的话删除分区的话会直接把数据给删除掉
    分区没有修改的功能
## 02 `MyCat`
### 为什么使用`Mycat`.
    1.代码与数据库紧耦合
    2.高访问量并发对数据库的压力
    3.读写请求数据不一致。最好放一个中间件MyCat。
### `MyCat`:基于`Cobar`进行二次开发
### `MyCat`作用：
    1.读写分离：主从同步
    2.数据分片：分库分表
### `MyCat`配置：详细信息见`py`文件
    配置文件修改：
    1.schema.xml：定义逻辑库，表，分片结点内容
    2.rule.xml：定义分片规则
    3.server.xml：定义用户及系统相关变量，如端口等
    4.sequence_db_conf.properties:全局序列定义
## 03 `主从复制`
### 原理：
    1、master将改变记录到二进制日志(Binary log)
    2、Slave访问Master将Master的Binary log 记录拷贝到Slave的中继日志(Relay log)
    3、Slave的SQL thread线程执行Relay log的事件，将改变执行一遍,同步到Slave的数据库中
### (1)`Master`配置:
    修改配置文件：sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
    # 主服务器唯一ID
    server-id=1
    #启用二进制日志
    log-bin=mysql-bin
    # 设置不要复制的数据库(可设置多个)
    binlog-ignore-db=mysql
    binlog-ignore-db=information_schema
    # 设置需要复制的数据库
    binlog-do-db=需要复制的主数据库名字
    # 设置logbin格式
    binlog_format=STATEMENT
    # 在作为从数据库的时候，有写入操作也要更新二进制日志文件
    log-slave-updates
### (2)`Slave`配置
    #从服务器唯一ID
    server-id=2
    #启用中继日志
    relay-log=mysql-relay
### (3)`Master2`、`Slave2`同理。修改id分别为`3`、`4`(双主从复制情况下)
### (4)重启 `mysql` 服务
### (5)两台主机上建立帐户并授权 `slave`
    #在主机Master1、Master2 MySQL里执行授权命令
    GRANT REPLICATION SLAVE ON *.* TO 'slave'@'%' IDENTIFIED BY '123456';
    #查询Master1、Master2的状态，分别记录下File和Position的值
    show master status;
### (6)在从机上配置需要复制的主机
    Slava1 复制 Master1，Slava2 复制 Master2，Master1 复制 Master2
    #复制主机的命令
    CHANGE MASTER TO MASTER_HOST='主机的IP地址',
    MASTER_USER='slave',
    MASTER_PASSWORD='123456',
    MASTER_LOG_FILE='mysql-bin.具体数字',MASTER_LOG_POS=具体值;
    #启动两台从服务器复制功能
    start slave;
    #查看从服务器状态
    show slave status\G;
    # Slave_IO_Running: Yes
    # Slave_SQL_Running: Yes
    显示配置成功
## 04 `读写分离`
### 不用针对每个表进行配置，只需要在schema.xml中的元素上增加dataNode="defaultDN"属性，并配置此dataNode对应的真实物理数据库的database，然后dataHost开启读写分离功能即可。配置实例详情见`Write-Read.py`文件
## 05 `日期分片`
## 常用的分片规则：
    1、取模
    2、分片枚举
    3、范围约定
    4、按日期（天）分片
### 项目主要采用按日期（天）分片，详细分片规则见`sharding_by_date.py`
## 06 `分库分表`
### 1、垂直分库：一个数据库由很多表的构成，每个表对应着不同的业务，垂直切分是指按照业务将表进行分类，分布到不同的数据库上面，这样也就将数据或者说压力分担到不同的库上面。详情配置见`py`文件
### 2、水平拆分：相对于垂直拆分，水平拆分不是将表做分类，而是按照某个字段的某种规则来分散到多个库之中，每个表中包含一部分数据。简单来说，可以将数据的水平切分理解为是按照数据行的切分，将表中的某些行切分到一个数据库，而另外的某些行又切分到其他的数据库中。
## 07 `全局序列`
### 在实现分库分表的情况下，数据库自增主键已无法保证自增主键的全局唯一。为此，Mycat 提供了全局 sequence，并且提供了包含本地配置和数据库配置等多种实现方式。
    1、本地文件
    2、时间戳方式
    3、数据库方式：使用最多
### 操作实例见`02 操作步骤.py`
## 08 `定时脚本`
### 更新完毕全局序列必须要重新启动MyCat才可以生效。每天定时开始执行脚本。判断主程序是否在运行，主程序在运行则等待主程序运行完毕在执行，主程序不在执行则开始运行脚本重启MyCat。
### 操作实例见`01 restart_script.py`
