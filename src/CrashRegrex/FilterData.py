# -*- coding: utf-8 -*-

import sys, os, time
import re
# import demjson
import  json
import  ElkReporter


class CrashData():

    def __init__(self, tMac,tTotal , tCrash):
        self.total = tTotal
        self.crashdict = tCrash
        self.mac = tMac
    def __init__(self):
          self.total = 0
          self.crashdict = {}
          self.mac = u""


def ReadFile(tFile):
    if tFile is None:
        return None
    if os.path.exists(tFile) is False:
        return None
    with open(tFile,"r+") as tFhandle:
        lConetent = tFhandle.read()
        lUnicode = lConetent.decode("utf-16")
        return  lUnicode


def FilterUserInfo(tData):
    if tData is None :
        return
    lMark = u"group by whole call stack"
    lPos = tData.find(lMark)
    lFinalPos = 0
    if lPos != -1:
        lPos2 = tData.find(lMark, lPos+len(lMark))
        if lPos2 != -1:
            lFinalPos = lPos2
    lReg = re.compile(ur"user\d{1,3};count:\d{1,4};mac:\w{12};crash\d{1,3}:\d+.*")
    lret = lReg.findall(tData,0,lPos)
    return  lret

def ConvertUserData(tList):
    lDict = {}
    for itor in tList:
        lmacinfo = re.findall(ur"mac:\w{12}",itor)
        lmac = lmacinfo[0][4:]
        lTotalCountinfo = re.findall(ur"count:\d{1,4}", itor)
        lTotal = lTotalCountinfo[0][6:]
        lCrashInfo = re.findall(ur"crash\d{1,3}:\d+",itor)
        lcrashDict = {}
        ltempDict = {}
        for item in lCrashInfo:
            ltemp = re.split(ur"\:", item)
            lcrashDict[ltemp[0]] =  int(ltemp[1])
        ltempDict[u"total"]= int(lTotal)
        ltempDict[u"crash"] = lcrashDict
        lDict[lmac] = ltempDict
    return  lDict

def ConvertUserDataByObj(tList):
    lList = []
    for itor in tList:
        lUnit = CrashData()
        lmacinfo = re.findall(ur"mac:\w{12}",itor)
        lUnit.mac = lmacinfo[0][4:]
        lTotalCountinfo = re.findall(ur"count:\d{1,4}", itor)
        lUnit.total = int(lTotalCountinfo[0][6:])
        lCrashInfo = re.findall(ur"crash\d{1,3}:\d+",itor)
        lcrashDict = {}
        for item in lCrashInfo:
            ltemp = re.split(ur"\:", item)
            lcrashDict[ltemp[0]] =  int(ltemp[1])
        lUnit.crashdict = lcrashDict
        lList.append(lUnit)
    return  lList


def FilterUserModule(tData):
    if tData is None:
        return

    lMark = u"group by whole call stack"
    lPos = tData.find(lMark)
    lFinalPos = 0
    if lPos != -1:
        lPos2 = tData.find(lMark, lPos+len(lMark))
        if lPos2 != -1:
            lFinalPos = lPos2

    lReg = re.compile(ur"crash\d+;count:\d+;module:[a-z0-9A-Z]+;function:[a-z0-9A-Z<>::_]*;")
    lret = lReg.findall(tData,0,lPos)
    return  lret


def ConvertUserModule(tList):
    lDict = {}
    for itor in tList:
        lCrashList = re.findall(ur"crash\d{1,3}", itor)
        lCrashHandle = lCrashList[0]
        lModuelList = re.findall(ur"module:[a-z0-9A-Z<>::_]*", itor)
        lModule = lModuelList[0][7:]
        lFunList = re.findall(ur"function:[a-z0-9A-Z<>::_]*", itor)
        lFunc = u""
        if len(lFunList) > 0:
            lFunc = lFunList[0][9:]
            lDict[lCrashHandle] = lModule +u"," + lFunc
        else:
            lDict[lCrashHandle] = lModule
    return lDict



def FilterCrashInfo2(tData):
    if tData is None:
        return

    lMark = u"group by whole call stack"
    lPos = tData.find(lMark)
    lFinalPos = 0
    if lPos != -1:
        lPos2 = tData.find(lMark, lPos + len(lMark))
        if lPos2 != -1:
            lFinalPos = lPos2
    lReg = re.compile(ur"\d{1,3} \w+, [a-z0-9A-Z<>::_]*")
    lret = lReg.findall(tData, 0, lPos)
    for itor in (lret):
        print  itor







def FilterBlock(tData):
    lReg = re.compile(ur"dmp\n+user count:\d((?:.|\n)*)")
    lret = lReg.findall(tData)
    # lret = lReg.findall(ur"user count:\d{1,4}(.*?)\n+group by whole call stack", tData, flags=re.MULTILINE)
    print  lret


def GenerateUserCrashData():
    lData =ReadFile("FxPartner_DumpStatistic_V4.54.0.460_20180109_daily.txt")
    lUserCrashInfo = ConvertUserDataByObj(FilterUserInfo(lData))
    lCrashDetail = ConvertUserModule(FilterUserModule(lData))
    lList = []
    for itor in lUserCrashInfo:
        if len(itor.crashdict) !=0:
            lDict = {}
            for lkey , lvalue in itor.crashdict.iteritems():
                if lCrashDetail.has_key(lkey) and len(lCrashDetail[lkey])> 0:
                    lDict[lCrashDetail[lkey]] = lvalue
            if len(lDict) > 0:
                itor.crashdict = lDict
                lList.append(itor)
    lRet = ConverntToJson(lList)

    lLimit = 0
    for itor in lRet:
        lLimit += 1
        if lLimit > 3:
            break
        ElkReporter.ReportElk(itor)


    return  lRet

def ConverntToJson(tList):
    lJson =[]

    for itor in tList:
        lUnit = GenerateJsonhead(u"crash",u"usercrash")
        lUnit[u"mac"] = itor.mac
        lUnit[u"total"] = itor.total
        lUnit[u"crash"] = itor.crashdict
        lJson.append(lUnit)
    return  lJson


def GenerateJsonhead(tProject , tLogType):
    lRoot = {}
    lRoot[u"group"] = u"fxclient"
    lRoot[u"log_time"] = u"0"
    lRoot[u"is_trusted_time"] = u"no"
    lRoot[u"project"] = tProject
    lRoot[u"log_type"] = tLogType
    lRoot[u"local_time"] = u""
    # custmize item
    lRoot[u"version"] = u""
    lRoot[u"date"] = u""
    return  lRoot



def GetToday(tFmt=u"%Y-%m-%d %H:%M:%S"):
    import datetime
    today = datetime.date.today()
    return unicode.format(tFmt%(today.year,today.month,today.day))



if __name__ == "__main__":
    print os.getcwd()
    lData =ReadFile("FxPartner_DumpStatistic_V4.54.0.460_20180109_daily.txt")
    # FilterUserInfo(lData)
    # FilterUserModule(lData)
    # FilterCrashInfo2(lData)
    # FilterBlock(lData)
    # lobj = ConvertUserData(FilterUserInfo(lData))
    # lobj = ConvertUserModule(FilterUserModule(lData))
    # print json.dumps(lobj,indent=4)
    ljson = GenerateUserCrashData()
    # print json.dumps(ljson , indent= 4)