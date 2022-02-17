# -*- coding: utf-8 -*-
# @Time : 2022/2/16 9:37
# @Author : O·N·E
# @File : 01 监控组件介绍安装配置.py
"""
1.简介
    Mycat-web是Mycat可视化运维的管理和监控平台，弥补了Mycat在监控上的空白。帮Mycat分担统计任务和配置管理任务。
    Mycat-web引入了ZooKeeper作为配置中心，可以管理多个节点。
2.安装
    (1)zookeeper
    MyCat-eye运行过程中需要依赖zookeeper，因此需要先安装zookeeper。下载zookeeper，然后解压，在conf/目录下找到zoo-sample.cfg，将其复制为zoo.cfg。
    zookeeper启动
    ./zkServer.sh start
    ZooKeeper服务端口为2181，查看服务是否已经启动
    netstat -ant | grep 2181
    (2)MyCat-web
    进入mycat-web的目录下运行启动命令
    ./start.sh & # 以后台形式进行启动
    Mycat-web服务端口为8082，查看服务已经启动
    netstat -ant | grep 8082
    (3)地址访问
    http://ip:8082/mycat/
3.MyCat-Web配置
    (1)注册中心配置ZooKeeper地址，配置后刷新页面，可见：
    (2)新增Mycat监控
    管理端口：9066；服务端口：8066；ip地址、用户名、密码需自己根据实际情况配置。
4.Mycat性能监控指标
    在 Mycat-web 上可以进行 Mycat 性能监控，例如：内存分享、流量分析、连接分析、活动线程分析等等。
"""
