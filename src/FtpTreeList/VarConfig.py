# -*- coding: utf-8 -*-
g_ftp_host="dumpupload.fanxing.com"
g_ftp_port="32100"
g_account="fanxingbanzou"
g_pwd="Kougou001"
g_help=u'''
-------------------
命令行使用说明：
用法：ftpDumpTaker.exe [版本号] [日期]
例如：ftpDumpTaker.exe 4.10.0.0  20170413

-------------------
'''

g_stepALL = u'''fTPDumpTaker V1.2 20170515
请选择过滤模式：
1. 按版本号和日期过滤   2 按昨天的版本号过滤
3. 按版本号过滤连续几天 4 按MAC和版本号过滤
请选择:（输入quit退出程序）
>'''

g_step_ver = u'''
请输入版本号：      例如:4.10.0.0
>'''

g_step_date = u'''
请输入日期：       例如:20170512
>'''

g_step_mac = u'''
请输入MAC：       例如:BC5FF4719ED4
>'''

g_serveral_days = u'''
请输入过去连续几天的值：      例如:2    (测试阶段)
假如今天为: 20170515,输入值为3, 则得到[20170514,20170513]
>'''


g_RED_COLOR='\033[1;31;48m'  #红 ，配置终端输出的颜色
g_BLUE_COLOR='\033[1;34;48m'  #红 ，配置终端输出的颜色
g_RES='\033[0m'
def Warming(tInfo):
    #print u"%s%s%s"%(g_RED_COLOR,tInfo ,g_RES),
    print tInfo ,

def Info(tInfo):
    #print u"%s%s%s"%(g_BLUE_COLOR,tInfo ,g_RES),
    print tInfo,