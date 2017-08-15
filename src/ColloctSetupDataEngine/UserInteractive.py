# -*- coding: utf-8 -*-



import os, sys
import time
import ProcessManager
import CollectData

g_Title = u'''
----------启动时长测试工具：V1.0---------
1: 全自动测试         2:读取日志获取平均时长
>'''



def UserInterActivate():
    while (True):
        print(g_Title),
        iIndex = raw_input()
        if iIndex == '1':
            ProcessManager.Run()
        elif iIndex == '2':
            CollectData.AnalyzeLog()
        elif iIndex == "q":
            break
        else:
            print(u"输入参数不正确,请输入[1-3之内的数值]")
        print ""

def Run():
    # try:
        UserInterActivate()
    # except Exception, ex:
    #     print ex
    #     print u"按回车键继续"
    #     raw_input()



if __name__ == "__main__":
    Run()