# -*- coding: utf-8 -*-
# @Time : 2022/1/11 17:01
# @Author : O·N·E
# @File : 02 MyCat配置.py
"""
配置：
MyCat:数据库的一个中间件
    原理：“拦截”功能，拦截用户发送的sql语句，首先对sql语句做了一些特定的分析，如分片分析，路由分析，读写分离
        缓存分析等，实现解耦操作
    配置文件修改：
        1.schema.xml：定义逻辑库，表，分片结点内容
        2.rule.xml：定义分片规则
        3.server.xml：定义用户及系统相关变量，如端口等
    1.server.xml 修改逻辑库的名字
    <user name="root" defaultAccount="true">
                <property name="password">123456</property>
                <property name="schemas">mycat</property>  # 逻辑库的名字 自行修改就好
                <property name="defaultSchema">TESTDB</property>
        </user>
        <user name="user">
                <property name="password">123456</property>
                <property name="schemas">mycat</property>
                <property name="readOnly">true</property>
                <property name="defaultSchema">TESTDB</property>
        </user>
    2.schema.xml 修改表
    <schema name="mycat" checkSQLschema="false" sqlMaxLimit="100" dataNode="dn1" randomDataNode="dn1">
    </schema>
        <dataNode name="dn1" dataHost="host1" database="text" />
        <dataHost name="host1" maxCon="1000" minCon="10" balance="0"
                          writeType="0" dbType="mysql" dbDriver="native" switchType="1"  slaveThreshold="100">
                <heartbeat>select user()</heartbeat> # 心跳检测
                <writeHost host="hostM1" url="192.168.81.140:3306" user="root"
                                   password="123456">
                        <readHost host="hostS1" url="1192.168.81.170:3306" user="root"
                                   password="123456" />
                </writeHost>
        </dataHost>
    3.MyCat测试
    mysql -u root -p -h 主机名 -P 端口号 进行访问其他虚拟机的数据库
    注意：要重启一个xshell服务进行开启
"""
