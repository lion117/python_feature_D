# -*- coding: utf-8 -*-

import sys, os, time
import  requests
import  json

def PostData(tUrl, tData):
    try:
        lRet = requests.post(tUrl,data=tData)
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
    lRoot[u"local_time"] = u""
    return  lRoot




class ElkHttp():
    @staticmethod
    def GenerateJsonContext(self, tProj, tLogType):
        lRoot = {}
        lRoot[u"group"] = u"fxclient"
        lRoot[u"log_time"] = u"0"
        lRoot[u"is_trusted_time"] = u"no"
        lRoot[u"project"] = tProj
        lRoot[u"log_type"] = tLogType
        lRoot[u"local_time"] = u""
        return  lRoot

    @staticmethod
    def AppendJson(self, tJson):
        lStrJson = json.dumps(tJson)
        ReportElk(lStrJson)





if __name__ == "__main__":
    print os.getcwd()
    print PostData(u"http://127.0.0.1:80/api",u"test")