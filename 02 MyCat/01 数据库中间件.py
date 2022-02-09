# -*- coding: utf-8 -*-
# @Time : 2022/2/9 16:47
# @Author : O·N·E
# @File : 01 数据库中间件.py
"""
数据库中间件介绍：
  (1)Cobar属于阿里B2B事业群，始于2008年，在阿里服役3年多，接管3000+个MySQL数据库的schema,集群日处理在线SQL请求50亿次以上。由于Cobar发起人的离职，Cobar停止维护。
  (2)Mycat是开源社区在阿里cobar基础上进行二次开发，解决了cobar存在的问题，并且加入了许多新的功能在其中。青出于蓝而胜于蓝。
  (3)DBLE企业级开源分布式中间件，以其简单稳定，持续维护，良好的社区环境和广大的群众基础得到了社区的大力支持
  (4)OneProxy基于MySQL官方的proxy思想利用c进行开发的，OneProxy是一款商业收费的中间件。舍弃了一些功能，专注在性能和稳定性上。
  (5)kingshard由小团队用go语言开发，还需要发展，需要不断完善。
  (6)Vitess是Youtube生产在使用，架构很复杂。不支持MySQL原生协议，使用需要大量改造成本。
  (7)Atlas是360团队基于mysql proxy改写，功能还需完善，高并发下不稳定。
  (8)MaxScale是mariadb（MySQL原作者维护的一个版本） 研发的中间件
  (9)MySQLRoute是MySQL官方Oracle公司发布的中间件
"""