# -*- coding: utf-8 -*-
# @Time : 2022/1/11 15:26
# @Author : O·N·E
# @File : 02 修改，删除分区方法.py
"""
删除分区：
    1.求余分区的情况下不会删除数据，数据会自定分配给其他的分区
    2.范围分区的话删除分区的话会直接把数据给删除掉

分区没有修改的功能
"""
import pymysql

host = 'localhost'
port = 3306
user = 'root'
password = '123456'
charset = 'utf8'


# 求余分区
# 修改key分区
def demo1():
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database='text',
        charset=charset
    )
    # 直接进行修改分区数量，分区的数量是追加的数量。2是追加的数量
    sql_Modify_partition = """alter table key_ add partition partitions 9"""
    cur = conn.cursor()
    cur.execute(sql_Modify_partition)
    # 删除分区
    sql_drop_partition = """alter table key_ coalesce partition 9"""
    cur = conn.cursor()
    cur.execute(sql_drop_partition)
    print("修改成功")


demo1()

# 修改hash分区
def demo2():
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database='text',
        charset=charset
    )
    sql_Modify_partition = """alter table hash add partition partitions 2"""
    cur = conn.cursor()
    cur.execute(sql_Modify_partition)
    print("修改成功")


demo2()


# 修改range()分区
def demo3():
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database='text',
        charset=charset
    )
    # 只能向后面进行追加.
    sql_Modify_partition = """alter table range_ add partition
    (
    partition 15_21 values less than(22)
    )"""
    cur = conn.cursor()
    cur.execute(sql_Modify_partition)
    # 删除分区 范围分区的话删除分区数据会丢失
    sql_Modify_partition = """alter table range_ drop partition 8_14"""
    cur = conn.cursor()
    cur.execute(sql_Modify_partition)
    print("修改成功")


demo3()

# 修改list分区
def demo4():
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database='text',
        charset=charset
    )
    sql_Modify_partition = """alter table list add partition
    (
    partition 29_31 values in (29,30,31)
    )"""
    cur = conn.cursor()
    cur.execute(sql_Modify_partition)
    print("修改成功")


demo4()
