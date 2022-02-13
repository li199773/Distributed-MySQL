"""
日期分片实例
此规则为按天分片。设定时间格式、范围。以imap_2022_01_27-imap_2022_29为例。
（1）修改schema.xml配置文件
<table name="imap_2022_01" primaryKey="id" dataNode='dn1' subTables="imap_2022_01_$27-29" rule="sharding-by-date" />

（2）修改rule.xml配置文件
<tableRule name="sharding_by_date">
    <rule>
        <columns>insert_time</columns>
        <algorithm>partbyday</algorithm>
    </rule>
</tableRule>

<function name="partbyday" class="io.mycat.route.function.PartitionByDate">
    <property name="dateFormat">yyyy-MM-dd</property>
    <property name="sBeginDate">2022-01-27</property>
    <!-- property name="sEndDate">2019-01-04</property -->
    <property name="sPartionDay">1</property>
</function>
 # columns：分片字段，algorithm：分片函数
# dateFormat：日期格式
# sBeginDate：开始日期
# sEndDate：结束日期,则代表数据达到了这个日期的分片后循环从开始分片插入，可以不进行设置
# sPartionDay：分区天数，即默认从开始日期算起，分隔x天一个分区

（3）重启 Mycat
"""