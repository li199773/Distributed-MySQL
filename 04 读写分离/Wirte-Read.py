# -*- coding: utf-8 -*-
# @Time : 2022/2/11 9:10
# @Author : O·N·E
# @File : Wirte-Read.py

"""
修改 Mycat 的配置文件 schema.xml
以smtp数据库为例，imap和pop3同理。
(1)修改<dataHost>的balance属性，通过此属性配置读写分离的类型.
负载均衡类型，目前的取值有4种：
    ①balance="0", 不开启读写分离机制，所有读操作都发送到当前可用的writeHost 上。
    ②balance="1"，全部的 readHost 与 stand by writeHost 参与 select 语句的负载均衡，简单的说，当双主双从模式(M1->S1，M2->S2，并且 M1 与 M2 互为主备)，正常情况下，M2,S1,S2 都参与 select 语句的负载均衡。
    ③balance="2"，所有读操作都随机的在 writeHost、readhost 上分发。
    ④balance="3"，所有读请求随机的分发到 readhost 执行，writerHost 不负担读压力。
设置Master写主机ip和Slave读主机ip，balance="1"，实现读写分离。
    <dataHost name="host1" maxCon="1000" minCon="10" balance="1" writeType="0" dbType="mysql" dbDriver="native" switchType="1" slaveThreshold="100" >
        <heartbeat>select user()</heartbeat>
        <writeHost host="hostM1" url="192.168.140.126:3306" user="root" password="123456">
            <readHost host="hostS1" url="192.168.140.127:3306" user="root" password="123456" />
        </writeHost>
        <writeHost host="hostM2" url="192.168.140.128:3306" user="root" password="123456">
            <readHost host="hostS2" url="192.168.140.129:3306" user="root" password="123456" />
        </writeHost>
    </dataHost>
(2)设置Master写主机ip和Slave读主机ip，balance="1"，实现读写分离。
#writeType="0": 所有写操作发送到配置的第一个writeHost，第一个挂了切到还生存的第二个
#writeType="1"，所有写操作都随机的发送到配置的 writeHost，1.5 以后废弃不推荐使用。
#writeHost，写主机ip
#readHost，读主机ip
#switchType="1": 1 默认值，自动切换。
#          -1 表示不自动切换
#          2 基于 MySQL 主从同步的状态决定是否切换。
Master1、Master2 互做备机，负责写的主机宕机，备机切换负责写操作，保证数据库读写分离高可用性。
"""