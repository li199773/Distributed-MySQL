# -*- coding: utf-8 -*-
# @Time : 2022/1/11 16:53
# @Author : O·N·E
# @File : 01 理论.py
"""
为什么使用Mycat
    1.代码与数据库紧耦合
    2.高访问量并发对数据库的压力
    3.读写请求数据不一致
    最好放一个中间件 MyCat
    MyCat:基于Cobar进行二次开发
MyCat作用：
    1.读写分离：主从同步
    2.数据分片：分库分表
分表的分类：
    1.垂直分表：
    垂直分表按照数据表字段进行拆分。
    两种拆分方式：
    (1)根据字段的使用频率,经常使用和不经常进行使用的进行区分开
    (2)根据字段是否为固定长度,固定长度,可变长度分开进行存储
    2.水平分表：
    水平分表按照数据进行拆分
垂直分库：按照不同的表（或者 Schema）来切分到不同的数据库（主机）之上，这种切可以称之为数据的垂直切分
水平分库：根据表中的数据的逻辑关系，将同一个表中的数据按照某种条 件拆分到多台数据库（主机）上面，这种切分称之为数 据的水平切分
1 垂直拆分（分库）
    实现垂直分库目的是为了，能够分摊主数据库的io压力，一般设置分出去的数据库为读，主服务器为写。主服务器和分服务器要实现主从复制的功能，这样就能实现读写分离，均衡数据库io，从而达到解决数据库瓶颈的目的
虽然分区也可以实现数据库的分表操作，但不是真正意义上的分表，还是在一个表上面进行操作
    真正的物理水平分表：一张表真实存在的进行分成多个表
    只是写入的情况下，可以写入2000万左右的数据
    读写的情况下，最好不好超过500万的数据量，超过500万要考虑分库分表的操作
"""
