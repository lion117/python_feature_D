# -*- coding: utf-8 -*-


from ftplib import FTP
import sys, getpass, os.path
import  ParaConfig


def UploadFile(tSrcFile):
    if os.path.exists(tSrcFile) is False:
        print u"%s file is not exist",tSrcFile
        return  False

    try :
        iFtpClient=FTP(ParaConfig.g_ftpUrl)
        iFtpClient.login(ParaConfig.g_ftpUser, ParaConfig.g_ftpPassword)
        # iFtpClient.cwd(remotepath)
        iFile=open(tSrcFile, 'rb')
        print os.path.basename(tSrcFile)
        #否则，如果参数 pasv 为假则关闭被动传输模式。
        #在被动模式打开的情况下，数据的传送由客户机启动，而不是由服务器开始。
        #这里要根据不同的服务器配置
        iFtpClient.set_pasv(0)
        iFtpClient.storbinary('STOR %s ' % os.path.basename(tSrcFile), iFile)
        iFile.close()
        iFtpClient.quit
        return True
    except Exception ,ex:
        print  ex
        return  False



if __name__ == "__main__":
    print(os.path.abspath("__file__"))
    print(os.getcwd())