# -*- coding: utf-8 -*-

import sys, os, time
import  requests
import  json
from AsynTaskFactory import *


def PostData(tUrl, tData):
    try:
        lRet = requests.post(tUrl,data=tData)
        print u"post data"
        return  lRet
    except Exception,ex:
        print ex.message
        return  None


def ReportElk(tData):
    if tData is None:
        return False
    lUrl = u"http://eof.log.fanxing.kugou.com/fxclient"
    lRet = PostData(lUrl, tData)
    if lRet is None:
        return  False
    else :
        return  True




def GenerateJsonhead(tProject , tLogType):
    lRoot = {}
    lRoot[u"group"] = u"fxclient"
    lRoot[u"log_time"] = u"0"
    lRoot[u"is_trusted_time"] = u"no"
    lRoot[u"project"] = tProject
    lRoot[u"log_type"] = tLogType
    lRoot[u"local_time"] = time.strftime(u"%Y-%m-%d %H:%M:%S", time.localtime()).decode("gbk")
    return  lRoot




class ElkHttp():
    # 创建一个有4个线程的线程池
    _threadPool = ThreadPoolManger(80)

    @staticmethod
    def GenerateJsonContext( tProj, tLogType):
        lRoot = {}
        lRoot[u"group"] = u"fxclient"
        lRoot[u"log_time"] = u"0"
        lRoot[u"is_trusted_time"] = u"no"
        lRoot[u"project"] = tProj
        lRoot[u"log_type"] = tLogType
        lRoot[u"local_time"] = time.strftime(u"%Y-%m-%d %H:%M:%S", time.localtime()).decode("gbk")

        return  lRoot

    @staticmethod
    def AppendJson( tJson):
        lStrJson = json.dumps(tJson)
        ReportElk(lStrJson)

    @classmethod
    def AppendJsonAysc(cls,tJson):
        lStrJson = json.dumps(tJson)
        cls._threadPool.addJob(ReportElk,*(lStrJson,))

    @classmethod
    def WaitForDone(cls):
        cls._threadPool.waitDone()









if __name__ == "__main__":
    lDate = time.strftime(u"%Y-%m-%d %H:%M:%S", time.localtime())
    print type(lDate.decode("gbk"))
    print os.getcwd()
    # print PostData(u"http://127.0.0.1:80/api",u"test")