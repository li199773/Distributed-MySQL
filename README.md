# MySQL + Python
## 01 MySQL分区:将数据分成几个表格，在数据库还是显示一个表格，不是真正的逻辑物理分表。
### 分区的分类：
    1.求余算法
    key算法：内置的key算法运算数字
        partition by key(id) partitions 2;
    hash算法：内置的hash算法运算数字
    2.范围区间
    list:范围
    range:区间
