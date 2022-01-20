# -*- coding: utf-8 -*-
# @Time : 2022/1/14 14:23
# @Author : O·N·E
# @File : 03 主从复制.py
"""
mysql主从复制原理：
    主机只允许只有一个，从机允许有多个
    主机将sql语句写入Binary.log日志中，从机读取该日志些到从机的Relay日志中去，从机在读取该日志再将sql语句写入
        到从机的数据库中
    存在大量的io操作，所以存在延时性的问题
主从复制配置：
    主机：192.168.81.140
    从机：192.168.81.171
    主机 ----> 从机

    给从机分配权限：目的是防止其他从机可以对主机进行读取操作:
    GRANT REPLICATION SLAVE ON *.* TO 'slave'@'%' IDENTIFIED BY '123456'; 给slave用户设置权限和密码

    查看主机的状态：
    show master status;
    记录主机的file和position

    在从机上配置需要复制的主机：
CHANGE MASTER TO MASTER_HOST='192.168.81.198',
MASTER_USER='slave',
MASTER_PASSWORD='123456',
MASTER_LOG_FILE='mysql_bin.000006',MASTER_LOG_POS=430;前者为file,后者为position

    从机启动slave;
    start slave;(假如之前配置过从机，先停止从机 stop slave;在重新设置即可 reset master)

    从机查看是否配置成功
    show slave status\G;数据太多按行进行输出
        Slave_IO_Running: Yes
        Slave_SQL_Running: Yes # 输出都为yes即可
        假如是全部克隆的话需要更改机器的uuid号码，不能为一样子

    读写分离配置：
        balance="0":不开启读分离机制
        balance="1":双主状从,负载平衡。既双主双从。
        balance="2":所有的操作随机在读写主机上分发
        balance="3":读请求随机分发到读主机上面执行，写主机不负担压力。既单主单从
"""
