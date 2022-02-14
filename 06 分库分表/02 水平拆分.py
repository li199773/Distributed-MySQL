# -*- coding: utf-8 -*-
# @Time : 2022/1/18 17:02
# @Author : O·N·E
# @File : 02 水平拆分.py
"""
    相比于垂直分库，分表更为复杂
    相对于垂直拆分，水平拆分不是将表做分类，而是按照某个字段的某种规则来分散到多个库之中，每个表中 包含一部分数据。简单来说，我们可以将数据的水平切分理解为是按照数据行的切分，就
是将表中的某些行切分 到一个数据库，而另外的某些行又切分到其他的数据库中。
    修改配置文件 schema.xml
    #为imap pop3 smtp库进行分表 设置数据节点为 dn1、dn2、dn3，并指定分片规则为 sharding-by-date
    <schema name="mycat" checkSQLschema="false" sqlMaxLimit="100">
            <table name="imap_2022_01" primaryKey="id" dataNode='dn1' subTables="imap_2022_01_$27-29" rule="sharding-by-date" />
            <table name='pop3_2022_01' primaryKey="id" dataNode='dn2' subTables="pop3_2022_01_$27-29" rule="sharding-by-date" />
            <table name='smtp_2022_01' primaryKey="id" dataNode='dn3' subTables="smtp_2022_01_$27-29" rule="sharding-by-date" >
            </table>
    </schema>
    # 按月日进行分库分表操作,subTables="imap_2022_01_$27-29" 日期

    # 设置每个节点的库名称和节点名称
    <dataNode name="dn1" dataHost="host1" database="imap_database" />
    <dataNode name="dn2" dataHost="host2" database="pop3_database" />
    <dataNode name="dn3" dataHost="host3" database="smtp_database" />


    # 设置每个节点的ip地址和配置
     <dataHost name="host1" maxCon="1000" minCon="10" balance="3"
                writeType="0" dbType="mysql" dbDriver="native" switchType="1"  slaveThreshold="100">
            <heartbeat>select user()</heartbeat>
            <writeHost host="hostM1" url="192.168.81.245:3306" user="root" password="123456" />
    </dataHost>

    <dataHost name="host2" maxCon="1000" minCon="10" balance="1"
                          writeType="0" dbType="mysql" dbDriver="native" switchType="1"  slaveThreshold="100">
            <heartbeat>select user()</heartbeat>
			<writeHost host="hostM2" url="192.168.81.216:3306" user="root" password="123456" />
    </dataHost>

    <dataHost name="host3" maxCon="1000" minCon="10" balance="1"
                writeType="0" dbType="mysql" dbDriver="native" switchType="1"  slaveThreshold="100">
            <heartbeat>select user()</heartbeat>
            <writeHost host="hostM3" url="192.168.81.242:3306" user="root" password="123456" />
    </dataHost>

    # 重启mycat
    ./mycat restart
"""
