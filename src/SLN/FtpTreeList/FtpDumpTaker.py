# -*- coding: utf-8 -*-



import os, sys
import time
import ftplib ,socket
import  VarConfig


class FtpTaker():
    def __init__(self):
        #定义公用变量
        self.RED_COLOR='\033[1;31;48m'  #红 ，配置终端输出的颜色
        self.BLUE_COLOR='\033[1;34;48m'  #红 ，配置终端输出的颜色
        self.RES='\033[0m'
    def FtpDownload(self, HostIP, SerPort, FtpUser, FtpPasswd, tLocalDir, tDate, tVer, tMac=""):
        iFtpObj = ftplib.FTP()
        try:
            iFtpObj.connect(host=HostIP, port=SerPort, timeout=10)
            print u'%s*****已经成功连接"%s"服务器FTP服务！%s' % (self.BLUE_COLOR,HostIP,self.RES)
        except (socket.error, socket.gaierror), e:
            print u'%s错误：无法访问"%s" FTP服务，请检查！错误代码为"%s"%s' % (self.RED_COLOR,HostIP,e,self.RES)
            exit()
        try:
            iFtpObj.login(user=FtpUser, passwd=FtpPasswd)
            print u'%s*****已经成功登陆"%s"服务器FTP服务！%s' % (self.BLUE_COLOR,HostIP,self.RES)
            print iFtpObj.getwelcome()#显示ftp服务器欢迎信息
        except (ftplib.error_perm), e:
            print u'%s错误：登陆失败！，请检查用户名"%s“密码"%s"是否正确！错误代码为"%s"%s' % (self.RED_COLOR,FtpUser,FtpPasswd,e,self.RES)
            exit()

        iServerList = iFtpObj.nlst()   #取FTP当前目录内容
        iDownloadList = self.FilterDirList(iServerList,tVer,tDate)
        bufsize = 1024
        iIndex =1
        print(u"即将下载dump文件")
        for line in iDownloadList:
            print "\r",
            print(u"正在下载第%d条"%iIndex),
            iIndex+=1
            FileName = open(tLocalDir + line, 'wb').write
            iFtpObj.retrbinary('RETR %s' % os.path.basename(line), FileName, bufsize)
        iFtpObj.quit()
        print u"%sFTP已经成功退出。%s"% (self.BLUE_COLOR,self.RES)



    def FilterDirList(self,tDirList ,tVer,tDate):
        iFilter ="FxPartner_CrashDump_V%s_%s"%(tVer,tDate)
        print (u"过滤条件为：%s"%iFilter)
        iResultList =[]
        for itor in tDirList:
            iReuslt = str(itor).find(iFilter)
            if  iReuslt>= 0:
                print itor
                iResultList.append(itor)

        print (u"共有数据 %d 条. 过滤获取数据 %d 条"%( len(tDirList), len(iResultList)))
        return  iResultList





if __name__ == "__main__":

    if len(sys.argv)!= 3:
        print(u"输入参数错误\r\n%s"%VarConfig.g_help)
        sys.exit()
    tVer = sys.argv[1]
    tDate= sys.argv[2]
    iLocalPath=str.format("./%s_%s/"%(tVer,tDate))
    if os.path.exists(iLocalPath) == False:  # 判断本地是否有该文件目录，如果没有，将创建
        try:
            os.mkdir(iLocalPath)
            print u"创建本地目录'%s'" % ( iLocalPath,)
        except:
            print u"无法创建本地目录'%s'，原因是无该盘符或者目录路径有问题，程序直接退出！" % ( iLocalPath)
            exit()  # 退出程序
    iFtpServer = FtpTaker()
    iFtpServer.FtpDownload(VarConfig.g_ftp_host, VarConfig.g_ftp_port,VarConfig.g_account, VarConfig.g_pwd,iLocalPath,tDate,tVer)
