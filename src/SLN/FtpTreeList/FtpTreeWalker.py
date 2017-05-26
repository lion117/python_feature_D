# -*- coding: utf-8 -*-



import os, sys
import time
import ftplib ,socket
import  VarConfig



def GetDirList():
    MyFTP = ftplib.FTP()
    try:
        MyFTP.connect(host=VarConfig.g_ftp_host, port=VarConfig.g_ftp_port, timeout=900000)
        print u'*****已经成功连接"%s"服务器FTP服务！' % (VarConfig.g_ftp_host)
    except (socket.error, socket.gaierror), e:
        print u'错误：无法访问"%s" FTP服务，请检查！错误代码为"%s"' % (VarConfig.g_ftp_host, e,)
        exit()
    try:
        MyFTP.login(user=VarConfig.g_account, passwd=VarConfig.g_pwd)
        print u'*****已经成功登陆服务器FTP服务！'
        print MyFTP.getwelcome()  # 显示ftp服务器欢迎信息
    except (ftplib.error_perm), e:
        print u'错误：登陆失败！，请检查用户名"%s“密码"%s"是否正确！错误代码为"%s"' % (VarConfig.g_account, VarConfig.g_pwd, e)
        exit()

    print u"正在遍历服务器文件"
    iFtpFileList = MyFTP.nlst()  # 取FTP当前目录内容
    print("there are total file counts %d" % len(iFtpFileList))
    return  iFtpFileList


def FilterDirList(tDirList , tDate,tVer,tMac=""):
    iFilter ="FxPartner_CrashDump_V%s_%s"%(tVer,tDate)
    iResultList =[]
    iIndex =0
    for itor in tDirList:
        iReuslt = str(itor).find(iFilter)
        if  iReuslt>= 0:
            print itor
            iResultList.append(itor)


    print "get total count  %d"%iResultList.__sizeof__()

if __name__ == "__main__":
    iList = GetDirList()
    # iList =["FxPartner_CrashDump_V5.5.5.5_20161118_184358_0632121745_Os6.1_64006A71BF7D.zip","FxPartner_CrashDump_V4.10.0.0_20170410_215826_0011176785_Os6.1_0250F24B2100.zip","FxPartner_CrashDump_V4.10.0.0_20170410_220546_0015758394_Os6.1_704D7B2FD22B.zip","FxPartner_CrashDump_V4.10.0.0_20170401_220546_0015758394_Os6.1_704D7B2FD22B.zip"]
    FilterDirList(iList , "20170410","4.10.0.0")
    print "finish"

    # for itor in iFtpFileList:
    #     print itor

