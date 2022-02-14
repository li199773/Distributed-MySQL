# -*- coding: utf-8 -*-
# @Time : 2022/1/18 16:57
# @Author : O·N·E
# @File : 01 垂直分库.py
"""
    将3个表imap_mail,pop3_mail,smtp_mail分别进行垂直分库到imap_database,pop3_database,smtp_database
1.定义三个节点和表名
    <table name='imap_mail' primaryKey="id" dataNode='dn1' />
    <table name='pop3_mail' primaryKey="id" dataNode='dn2' />
    <table name='smtp_mail' primaryKey="id" dataNode='dn3'>
    </table>
2.插入对应数据库的节点设置
    <dataNode name="dn1" dataHost="host1" database="imap_database" />
    <dataNode name="dn2" dataHost="host2" database="pop3_database" />
    <dataNode name="dn3" dataHost="host3" database="smtp_database" />
3.主机地址设置
    <dataHost name="host1" maxCon="1000" minCon="10" balance="1"
                      writeType="0" dbType="mysql" dbDriver="native" switchType="1"  slaveThreshold="100">
            <heartbeat>select user()</heartbeat>
            <writeHost host="hostM1" url="192.168.81.194:3306" user="root" password="123456" />
    </dataHost>

    <dataHost name="host2" maxCon="1000" minCon="10" balance="1"
                      writeType="0" dbType="mysql" dbDriver="native" switchType="1"  slaveThreshold="100">
            <heartbeat>select user()</heartbeat>
            <writeHost host="hostM1" url="192.168.81.200:3306" user="root" password="123456" />
    </dataHost>

    <dataHost name="host3" maxCon="1000" minCon="10" balance="1"
                      writeType="0" dbType="mysql" dbDriver="native" switchType="1"  slaveThreshold="100">
            <heartbeat>select user()</heartbeat>
            <writeHost host="hostM1" url="192.168.81.199:3306" user="root" password="123456" />
    </dataHost>

"""
