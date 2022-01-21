# -*- coding: utf-8 -*-
# @Time : 2022/1/17 15:59
# @Author : O·N·E
# @File : 04 双主双从.py
"""
1.主机配置：
    # 主机1
    server-id=1
    log-bin=mysql-bin
    binlog-ignore-db=mysql
    binlog-do-db=text
    binlog-format=STATEMENT

    log-slave=updates # 主机挂掉之后为从机也要写日志
    auto-increment-increment=2：自增长的步长
    auto-increment-offset=1：自增长的开始值
    # 主机3
    server-id=3
    log-bin=mysql-bin
    binlog-ignore-db=mysql
    binlog-do-db=text
    binlog-format=STATEMENT

    log-slave-updates
    auto-increment-increment=2
    auto-increment-offset=2

    # 从机2
    server_id=2
    relay_log=mysql_relay
    # 从机4
    server_id=4
    relay_log=mysql_relay
2.重启所有机器的mysql即可
    service mysql restart
    查看mysql的活动状态
    service mysql status
3.修改每台机器的uuid 保证每一台虚拟机的uuid不能一样
4.为两台主机都要添加用户
    GRANT REPLICATION SLAVE ON *.* TO 'slave'@'%' IDENTIFIED BY '123456';
    查看所有的用户
    use mysql;
    select host,user from user;
5.两个主机进行相互复制
CHANGE MASTER TO MASTER_HOST='192.168.81.198',
MASTER_USER='slave',
MASTER_PASSWORD='123456',
CHANGE MASTER TO MASTER_LOG_FILE='mysql_bin.000002',MASTER_LOG_POS=824;
# 设置为自己的ip和密码
CHANGE MASTER TO MASTER_HOST='192.168.81.199',
MASTER_USER='slave',
MASTER_PASSWORD='123456',
MASTER_LOG_FILE='mysql_bin.000001',MASTER_LOG_POS=154;


问题1：
    set global sql_slave_skip_counter=1;

6.mycat启动
    # 主从1
    <writeHost host="hostM1" url="192.168.81.194:3306" user="root"
                    password="123456">
            <readHost host="hostS1" url="192.168.81.200:3306" user="root"
                    password="123456" />
    </writeHost>
    # 主从2
    <writeHost host="hostM2" url="192.168.81.199:3306" user="root"
                    password="123456">
            <readHost host="hostS2" url="192.168.81.195:3306" user="root"
                    password="123456" />
    </writeHost>
7.mycat机进入
    mysql -uroot -p -h -P8066
    由于设置的balance为1，是双主双从的配置，读写分离，插入数据
    insert into demo3 values(1,@@hostname) # hostname 为每一台主机的名字，克隆的主机修改不一样子的名字即可
    插入hostname进行查询会有区别。

全部配置文件
<?xml version="1.0"?>
<!DOCTYPE mycat:schema SYSTEM "schema.dtd">
<mycat:schema xmlns:mycat="http://io.mycat/">

        <schema name="mycat" checkSQLschema="false" sqlMaxLimit="100" dataNode="dn1" randomDataNode="dn1">
                <!-- auto sharding by id (long) -->
                <!--splitTableNames 启用<table name 属性使用逗号分割配置多个表,即多个表使用这个配置-->
<!--fetchStoreNodeByJdbc 启用ER表使用JDBC方式获取DataNode-->
        </schema>
        <dataNode name="dn1" dataHost="host1" database="text" />
        <dataHost name="host1" maxCon="1000" minCon="10" balance="1"
                          writeType="0" dbType="mysql" dbDriver="native" switchType="1"  slaveThreshold="100">
                <heartbeat>select user()</heartbeat>
                <!-- can have multi write hosts -->
                <writeHost host="hostM1" url="192.168.81.194:3306" user="root"
                                password="123456">
                        <readHost host="hostS1" url="192.168.81.200:3306" user="root"
                                password="123456" />
                </writeHost>
                <writeHost host="hostM2" url="192.168.81.199:3306" user="root"
                                password="123456">
                        <readHost host="hostS2" url="192.168.81.195:3306" user="root"
                                password="123456" />
                </writeHost>

        </dataHost>
</mycat:schema>

"""
