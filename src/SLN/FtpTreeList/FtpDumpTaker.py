# -*- coding: utf-8 -*-



import os, sys
import time
import ftplib ,socket
import  VarConfig
import  subprocess

class FtpTaker():
    def __init__(self):
        #定义公用变量
        self.RED_COLOR='\033[1;31;48m'  #红 ，配置终端输出的颜色
        self.BLUE_COLOR='\033[1;34;48m'  #红 ，配置终端输出的颜色
        self.RES='\033[0m'
        self.HostIP = VarConfig.g_ftp_host
        self.SerPort = VarConfig.g_ftp_port
        self.FtpUser = VarConfig.g_account
        self.FtpPasswd = VarConfig.g_pwd
        self._isLogin = False
        self._FtpObj = ftplib.FTP()
        try:
            self._FtpObj.connect(host=self.HostIP, port=self.SerPort, timeout=10)
            print u'%s*****已经成功连接"%s"服务器FTP服务！%s' % (self.BLUE_COLOR, self.HostIP, self.RES)
        except (socket.error, socket.gaierror), e:
            print u'%s错误：无法访问"%s" FTP服务，请检查！错误代码为"%s"%s' % (self.RED_COLOR, self.HostIP, e, self.RES)
            exit()
        try:
            self._FtpObj.login(user=self.FtpUser, passwd=self.FtpPasswd)
            print u'%s*****已经成功登陆"%s"服务器FTP服务！%s' % (self.BLUE_COLOR, self.HostIP, self.RES)
            self._isLogin = True
        except (ftplib.error_perm), e:
            print u'%s错误：登陆失败！，请检查用户名"%s“密码"%s"是否正确！错误代码为"%s"%s' % (
            self.RED_COLOR, self.FtpUser, self.FtpPasswd, e, self.RES)
            exit()


    def FtpDownload(self,  tLocalDir,tType, tDate="", tVer="", tMac=""):
        if self._isLogin is False:
            print(u"登录ftp服务器失败,请检测后在重新下载")
            return

        iServerList = self._FtpObj.nlst()   #取FTP当前目录内容
        if tType == 0 and len(tDate) !=0 and len(tVer)!=0:
            iDownloadList = self.FilterDirListByDateVer(iServerList, tVer, tDate)
        elif tType ==1and len(tMac)!=0:
            iDownloadList = self.FilterDirListByMac(iServerList, tMac)
        elif tType == 2 and len(tVer)!=0 and len(tMac)!=0 :
            iDownloadList = self.FilterDirListByMacVer(iServerList, tMac, tVer)
        else:
            print(u"tType  error %d"%tType)
            return

        bufsize = 1024
        iIndex =1

        for line in iDownloadList:
            print "\r",
            print(u"正在下载第%d条"%iIndex),
            iIndex+=1
            FileName = open(tLocalDir + line, 'wb').write
            self._FtpObj.retrbinary('RETR %s' % os.path.basename(line), FileName, bufsize)
        self._FtpObj.quit()
        print(u"")
        print u"下载完成\n%sFTP已经成功退出。%s"% (self.BLUE_COLOR,self.RES)
        # os.startfile(tLocalDir)



    def FilterDirListByDateVer(self, tDirList, tVer, tDate):
        iFilter ="FxPartner_CrashDump_V%s_%s"%(tVer,tDate)
        print (u"过滤条件为：%s"%iFilter)
        iResultList =[]
        for itor in tDirList:
            iReuslt = str(itor).find(iFilter)
            if  iReuslt>= 0:
                # print itor
                iResultList.append(itor)

        print (u"共有数据 %d 条. 过滤获取数据 %d 条"%( len(tDirList), len(iResultList)))
        return  iResultList

    def FilterDirListByMac(self,tDirList,tMac):
        iFilter = tMac
        print (u"过滤条件为MAC：%s" % iFilter)
        iResultList = []
        for itor in tDirList:
            iReuslt = str(itor).find(iFilter)
            if iReuslt >= 0:
                iResultList.append(itor)
        print (u"共有数据 %d 条. 过滤获取数据 %d 条" % (len(tDirList), len(iResultList)))
        return iResultList


    def FilterDirListByMacVer(self,tDirList,tMac,tVer):
            print (u"过滤条件mac：%s 版本号为：%s" % (tMac, tVer))
            iResultList = []
            iSecondList=[]
            for itor in tDirList:
                iReuslt = str(itor).find(tMac)
                if iReuslt >= 0:
                    iResultList.append(itor)

            for itor1 in iResultList:
                iReuslt = str(itor1).find(tVer)
                if iReuslt >= 0:
                    iSecondList.append(itor1)
            print (u"共有数据 %d 条. 过滤获取数据 %d 条" % (len(tDirList), len(iSecondList)))
            return iSecondList


def UserInterActivate():

    while(True):
        VarConfig.Warming(VarConfig.g_stepALL)
        iIndex = raw_input()
        if iIndex == '1':
            VarConfig.Info(VarConfig.g_step_ver)
            iVer = raw_input()
            VarConfig.Info(VarConfig.g_step_date)
            iDate = raw_input()
            iLocalPath = str.format("./%s_%s/" % (iVer, iDate))
            if os.path.exists(iLocalPath) == False:  # 判断本地是否有该文件目录，如果没有，将创建
                try:
                    os.mkdir(iLocalPath)
                    print u"创建本地目录'%s'" % (iLocalPath,)
                except:
                    print u"无法创建本地目录'%s'，原因是无该盘符或者目录路径有问题，程序直接退出！" % (iLocalPath)
                    exit()  # 退出程序
            iFtpServer = FtpTaker()
            iFtpServer.FtpDownload(iLocalPath, 0, tDate=iDate, tVer=iVer)

        elif iIndex == '2':
            iYesterday= GetLastday()
            print (u"昨天日期是：%s", GetLastday())
            VarConfig.Info(VarConfig.g_step_ver)
            iVer = raw_input()
            iLocalPath = str.format("./%s_%s/" % (iVer, iYesterday))
            if os.path.exists(iLocalPath) == False:  # 判断本地是否有该文件目录，如果没有，将创建
                try:
                    os.mkdir(iLocalPath)
                    print u"创建本地目录'%s'" % (iLocalPath,)
                except:
                    print u"无法创建本地目录'%s'，原因是无该盘符或者目录路径有问题，程序直接退出！" % (iLocalPath)
                    exit()  # 退出程序
            iFtpServer = FtpTaker()
            iFtpServer.FtpDownload(iLocalPath, 0, tDate=iYesterday, tVer=iVer)

        elif iIndex == '3':
            VarConfig.Info(VarConfig.g_serveral_days)
            iDays = raw_input()
            VarConfig.Info(VarConfig.g_step_ver)
            iVer = raw_input()
            for iTheDay in range(iDays):
                iLocalPath = str.format("./%s_%s/" % (iVer, iTheDay))
                if os.path.exists(iLocalPath) == False:  # 判断本地是否有该文件目录，如果没有，将创建
                    try:
                        os.mkdir(iLocalPath)
                        print u"创建本地目录'%s'" % (iLocalPath,)
                    except:
                        print u"无法创建本地目录'%s'，原因是无该盘符或者目录路径有问题，程序直接退出！" % (iLocalPath)
                        exit()  # 退出程序
                iFtpServer = FtpTaker()
                iFtpServer.FtpDownload(iLocalPath, 0, tDate=iTheDay, tVer=iVer)

        elif iIndex == '4':
            VarConfig.Info(VarConfig.g_step_ver)
            iVer = raw_input()
            VarConfig.Info(VarConfig.g_step_mac)
            iMac = raw_input()
            iLocalPath = str.format("./%s_%s/" % (iVer, iMac))
            if os.path.exists(iLocalPath) == False:  # 判断本地是否有该文件目录，如果没有，将创建
                try:
                    os.mkdir(iLocalPath)
                    print u"创建本地目录'%s'" % (iLocalPath,)
                except:
                    print u"无法创建本地目录'%s'，原因是无该盘符或者目录路径有问题，程序直接退出！" % (iLocalPath)
                    exit()  # 退出程序
            iFtpServer = FtpTaker()
            iFtpServer.FtpDownload(iLocalPath, 2, tMac=iMac, tVer=iVer)
        elif iIndex == "quit":
            break
        else:
            VarConfig.Warming(u"输入参数不正确,请输入[1-3之内的数值]")



def GetLastday(tDays= 1):
    import datetime
    today = datetime.date.today()
    oneday = datetime.timedelta(days=tDays)
    iLastday = today - oneday
    # iStrYesterday = time.strftime("%y%m%d",iLastday)
    return  iLastday.strftime("%Y%m%d")


if __name__ == "__main__":

    if len(sys.argv) > 1:
        print VarConfig.g_help
    if len(sys.argv)== 3:
        tVer = sys.argv[1]
        tDate = sys.argv[2]
        iLocalPath = str.format("./%s_%s/" % (tVer, tDate))
        if os.path.exists(iLocalPath) == False:  # 判断本地是否有该文件目录，如果没有，将创建
            try:
                os.mkdir(iLocalPath)
                print u"创建本地目录'%s'" % (iLocalPath,)
            except:
                print u"无法创建本地目录'%s'，原因是无该盘符或者目录路径有问题，程序直接退出！" % (iLocalPath)
                exit()  # 退出程序
        iFtpServer = FtpTaker()
        iFtpServer.FtpDownload(iLocalPath, 0,tDate, tVer)
    else:
        UserInterActivate()
