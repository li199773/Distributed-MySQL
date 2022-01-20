# MySQL + Python
## 01 `MySQL分区`:将数据分成几个表格，在数据库还是显示一个表格，不是真正的逻辑物理分表。
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
### MyCat作用：
    1.读写分离：主从同步
    2.数据分片：分库分表
### `MyCat`配置：详细信息见`py`文件
    配置文件修改：
    1.schema.xml：定义逻辑库，表，分片结点内容
    2.rule.xml：定义分片规则
    3.server.xml：定义用户及系统相关变量，如端口等
