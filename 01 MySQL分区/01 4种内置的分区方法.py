# -*- coding: utf-8 -*-
# @Time : 2022/1/11 10:33
# @Author : O·N·E
# @File : 01 4种内置的分区方法.py
"""
分区的分类：
    1.求余算法
    key算法：内置的key算法运算数字
    hash算法：内置的hash算法运算数字
    2.范围区间
    list:范围
    range:区间
"""
import pymysql

host = 'localhost'
port = 3306
user = 'root'
password = '123456'
charset = 'utf8'


# 求余分区
# demo1 按照key进行分区
def demo1():
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database='text',
        charset=charset
    )
    sql_create_table = """create table if not exists key_(
                            id int primary key auto_increment,
                            username varchar(30) not null
                            )partition by key(id) partitions 2;
                        """
    cur = conn.cursor()
    cur.execute(sql_create_table)
    sql_insert_data = """insert into key_ values(not null,'zhangsan')"""
    for i in range(10000):
        cur.execute(sql_insert_data)
        conn.commit()
    print("插入成功")


demo1()  # 创建成功之后源文件路径会显示两个的数据库，但是在navicat中还是会显示一个表格


# demo2 按照hash进行分区:跟之前的key分区差不多是一样子的
def demo2():
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database='text',
        charset=charset
    )
    sql_create_table = """create table if not exists hash(
                            id int primary key auto_increment,
                            username varchar(30) not null
                            )partition by hash(id) partitions 2;
                        """
    cur = conn.cursor()
    cur.execute(sql_create_table)
    sql_insert_data = """insert into hash values(not null,'zhangsan')"""
    for i in range(10000):
        cur.execute(sql_insert_data)
        conn.commit()
    print("插入成功")


demo2()


# 范围分区
# demo3 按照range进行分区
def demo3():
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database='text',
        charset=charset
    )
    sql_create_table = """create table if not exists range_(
                            id int not null auto_increment,
                            username varchar(30) not null,
                            num int not null,
                            primary key(id,num)
                            )
                            partition by range(num)
                            (
                            partition 1_7 values less than(8),
                            partition 8_14 values less than(15)
                            );
                        """
    cur = conn.cursor()
    cur.execute(sql_create_table)
    sql_insert_data = """insert into range_ values(not null,'zhangsan',8)"""
    for i in range(10000):
        cur.execute(sql_insert_data)
        conn.commit()
    print("插入成功")


demo3()  # 7天分一个表


demo4
# 按照list进行分区, 跟range分区类似


def demo4():
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database='text',
        charset=charset
    )
    sql_create_table = """create table if not exists list(
                            id int not null auto_increment,
                            username varchar(30) not null,
                            num int not null,
                            primary key(id,num)
                            )
                            partition by list(num)
                            (
                            partition 1_7 values in(1,2,3,4,5,6,7),
                            partition 8_14 values in(8,9,10,11,12,13,14),
                            partition 15_21 values in(15,16,17,18,19,20,21),
                            partition 22_28 values in(22,23,24,25,26,27,28)
                            )
                        """
    cur = conn.cursor()
    cur.execute(sql_create_table)
    sql_insert_data = """insert into list values(not null,'zhangsan',11)"""
    for i in range(10000):
        cur.execute(sql_insert_data)
        conn.commit()
    print("插入成功")


demo4()  # 7天分一个表
