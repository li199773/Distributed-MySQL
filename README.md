# MySQL + Python
## 01 MySQL分区:将数据分成几个表格，在数据库还是显示一个表格，不是真正的逻辑物理分表。
### 分区的分类：
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
## 02 MyCat
### 
