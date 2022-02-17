# -*- coding: utf-8 -*-
# @Time : 2022/2/16 9:34
# @Author : O·N·E
# @File : 01 restart_script.py
"""
更新完毕全局序列必须要重新启动MyCat才可以生效。
# 每天定时开始执行脚本。判断主程序是否在运行，主程序在运行则等待主程序运行完毕在执行，主程序不在执行则开始运行脚本重启MyCat。
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text
def mycat_restart():
    MycatRestartCmd = "/usr/local/mycat/bin/mycat restart"
    execCmd(MycatRestartCmd)
    print("ok")

if __name__ == '__main__':
    while True:
        time.sleep(2)
        #最后一个|是导向grep过滤掉grep进程：因为grep查看程序名也是进程，会混到查询信息里
        programIsRunningCmd = "ps -ef|grep demo1.py|grep -v grep"
        programIsRunningCmdAns = execCmd(programIsRunningCmd)
        ansLine = programIsRunningCmdAns.split('\n')
        # 判断如果返回行数>2则说明python脚本程序已经在运行，打印提示信息结束程序，否则运行脚本代码doSomething()
        if len(ansLine) > 2:
            print("programName have been Running")
        else:
            mycat_restart()
            Break
"""
