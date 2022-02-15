# -*- coding: utf-8 -*-
# @Time : 2022/2/15 9:28
# @Author : O·N·E
# @File : 02 操作步骤.py
"""
操作步骤：
①建库序列脚本
#在 dn1 上创建全局序列表
CREATE TABLE MYCAT_SEQUENCE (NAME VARCHAR(50) NOT NULL,current_value INT NOT
NULL,increment INT NOT NULL DEFAULT 100, PRIMARY KEY(NAME)) ENGINE=INNODB;

#创建全局序列所需函数
DELIMITER $$
CREATE FUNCTION mycat_seq_currval(seq_name VARCHAR(50)) RETURNS VARCHAR(64)
DETERMINISTIC
BEGIN
DECLARE retval VARCHAR(64);
SET retval="-999999999,null";
SELECT CONCAT(CAST(current_value AS CHAR),",",CAST(increment AS CHAR)) INTO retval FROM
MYCAT_SEQUENCE WHERE NAME = seq_name;
RETURN retval;
END $$
DELIMITER ;

DELIMITER $$
CREATE FUNCTION mycat_seq_setval(seq_name VARCHAR(50),VALUE INTEGER) RETURNS
VARCHAR(64)
DETERMINISTIC
BEGIN
UPDATE MYCAT_SEQUENCE
SET current_value = VALUE
WHERE NAME = seq_name;
RETURN mycat_seq_currval(seq_name);
END $$
DELIMITER ;

DELIMITER $$
CREATE FUNCTION mycat_seq_nextval(seq_name VARCHAR(50)) RETURNS VARCHAR(64)
DETERMINISTIC
BEGIN
UPDATE MYCAT_SEQUENCE
SET current_value = current_value + increment WHERE NAME = seq_name;
RETURN mycat_seq_currval(seq_name);
END $$
DELIMITER ;

#初始化序列表记录
INSERT INTO MYCAT_SEQUENCE(NAME,current_value,increment) VALUES ('ORDERS', -99,100);
# 设置初始为1，步长取值为100，即每次分配100号段。
②修改 Mycat 配置
#修改sequence_db_conf.properties
# ORDERS这个序列在dn1这个节点上，具体dn1节点在host配置，请参考schema.xml，根据实际配置情况进行配置即可。

③修改server.xml
#全局序列类型：0-本地文件，1-数据库方式，2-时间戳方式。此处修改成1。

④MySQL事件
create event if not exists update_event ON SCHEDULE EVERY 1 DAY STARTS '2022-01-27 00:00:00' on completion not preserve comment '更新current_value' do update MYCAT_SEQUENCE set current_value=-99;
# 每天定时任务将全局序列置0
"""
