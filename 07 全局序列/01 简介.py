# -*- coding: utf-8 -*-
# @Time : 2022/2/15 9:26
# @Author : O·N·E
# @File : 01 简介.py
"""
在实现分库分表的情况下，数据库自增主键已无法保证自增主键的全局唯一。为此，Mycat 提供了全局 sequence，并且提供了包含本地配置和数据库配置等多种实现方式
(1)本地文件
此方式 Mycat 将 sequence 配置到文件中，当使用到 sequence 中的配置后，Mycat 会更新classpath 中的 sequence_conf.properties 文件中 sequence 当前的值。
① 优点：本地加载，读取速度较快
② 缺点：抗风险能力差，Mycat 所在主机宕机后，无法读取本地文件。
(2)时间戳方式
全局序列ID= 64 位二进制 (42(毫秒)+5(机器 ID)+5(业务编码)+12(重复累加) 换算成十进制为 18 位数的long 类型，每毫秒可以并发 12 位二进制的累加。
① 优点：配置简单
② 缺点：18 位 ID 过长
(3)数据库方式：使用最多
实现方式：
在数据库中建立一张表MYCAT_SEQUENCE ，用于存放序列sequence 名称(name)，sequence 当前值(current_value)，步长(increment int 类型每次读取多少个 sequence。
原理步骤：
①初次获取sequence时，根据传入的序列名称，从数据库表中获取current_value,increment到MyCat中，并将数据库中的current_value更新为current_value + increment。
②MyCat将读取到的current_value + increment作为本次的序列，在下次使用时，将序列的值 + 1，当使用increment次后，重复第一个步骤。
③MyCat负责维护序列表MYCAT_SEQUENCE，当用到序列时，往数据库表中插入一条记录即可。如果某次读取完的序列还没有用完数据库就崩了，那么剩余的没有使用的序列将会被废弃掉。
"""
