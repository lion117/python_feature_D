# -*- coding: utf-8 -*-

import sys, os, time
import datetime
import requests
from  ElkReporter import  ElkHttp


class DumpInfoRequest():

    def ReadInfoFromSrv(self, tDate):
        lUrl = u"http://dumpupload.fanxing.com/fxlist.php?date=%s&format=json"%tDate
        lList = self.ParseFiles(lUrl)
        return lList

    def ReadDumpFromSrv(self, tList):
        lRetList = self.Filter(tList, self.GenerateFilter())
        return  lRetList

    def ParseFiles(self, url):
        r = requests.get(url)
        if r.status_code != 200:
            print (u"visit web failed: error code: %d"%r.status_code)
            return  None
        lJsonOb = r.json()
        if lJsonOb['code'] != 0 :
            print (u"parse json error : %s"%lJsonOb['msg'])
            return  None
        lWebUrl = lJsonOb['filePath']
        lArray = []
        for itor in lJsonOb['fileName']:
            lArray.append(os.path.join(lWebUrl,itor))
        return lArray

    @staticmethod
    def ReadDumpList(tDate):
        lobj = DumpInfoRequest()
        lList = lobj.ReadInfoFromSrv(tDate)
        lNewList = lobj.ReadDumpFromSrv(lList)
        return  lNewList

    @staticmethod
    def Test():
        lobj = DumpInfoRequest()
        lList = lobj.ReadInfoFromSrv(u"2018-01-26")
        print lobj.ReadDumpFromSrv(lList)

    @staticmethod
    def GenerateFilter():
        lFilter = unicode.format(u"Partner_CrashDump_V")
        return  lFilter

    @staticmethod
    def Filter(tList, tFilter):
        if tFilter is None:
            return  tList
        lRetList = []
        for itor in tList:
            iReuslt = itor.find(tFilter)
            if iReuslt >= 0:
                lRetList.append(itor)
        print (u"共有%d个文件,过滤到%d个文件"%(len(tList),len(lRetList)))
        return lRetList




class AnalyzeListDump():
    @staticmethod
    def AnalizeDump(tList):
        for itor in tList:
            if itor.find(u"FxPartner_CrashDump_V") == -1:
                return
            lStr = itor.upper()
            lIndexList = []
            lMark = u"_"
            lStartPos = lStr.find(lMark, 0)
            while lStartPos != -1:
                lIndexList.append(lStartPos)
                lStartPos = lStr.find(lMark, lStartPos + 1)
            if len(lIndexList) != 7:
                print u"invalid item ", lStr
                return
            lEndPos = lStr.find(u".ZIP")
            lDict = ElkHttp.GenerateJsonContext(u"crash", u"alldump")
            lDict[u"version"] = lStr[lIndexList[1] + 2: lIndexList[2]]
            lDict[u"date"] = int(lStr[lIndexList[2] + 1: lIndexList[3]])
            lDict[u"time"] = int(lStr[lIndexList[3] + 1: lIndexList[4]])
            lDict[u"os"] = lStr[lIndexList[5] + 1: lIndexList[6]]
            lDict[u"mac"] = lStr[lIndexList[6] + 1: lEndPos]
            # print lDict
            ElkHttp.AppendJsonAysc(lDict)
        ElkHttp.WaitForDone()

    @staticmethod
    def Test():
        lStr = u"FxPartner_CrashDump_V4.56.0.480_20180126_133940_0012743269_Os6.1_3497F6A3C3D3.zip"
        lStr = lStr.upper()
        lIndexList = []
        lMark = u"_"
        lStartPos = lStr.find(lMark,0)
        while lStartPos != -1 :
            lIndexList.append(lStartPos)
            lStartPos = lStr.find(lMark, lStartPos+1)
        if len(lIndexList) != 7:
            print u"invalid item ", lStr
            return
        lEndPos = lStr.find(u".ZIP")
        lDict = ElkHttp.GenerateJsonContext(u"crash", u"alldump")
        lDict[u"version"] = lStr[lIndexList[1]+2: lIndexList[2]]
        lDict[u"date"] = int(lStr[lIndexList[2]+1: lIndexList[3]])
        lDict[u"time"] = int(lStr[lIndexList[3]+1: lIndexList[4]])
        lDict[u"os"] = lStr[lIndexList[5]+1: lIndexList[6]]
        lDict[u"mac"] = lStr[lIndexList[6]+1: lEndPos]
        # print lDict
        ElkHttp.AppendJsonAysc(lDict)
        ElkHttp.WaitForDone()






class MrgListDumpAnalyzer():
    def __init__(self):
        self._endDate = 20180120
        self._startDate = int(datetime.date.today().strftime(u"%Y%m%d"))

    def AnalyzeByDateRange(self):
        lList = []
        endDate = 20180120
        startDate = int(datetime.date.today().strftime(u"%Y%m%d"))
        lDiff = startDate - endDate
        for itor in range(1, lDiff + 1):
            lDate = GetSpecailDate(itor, tFmt=u"%Y-%m-%d").decode("gbk")
            lList.append(lDate)
            lDumpList = DumpInfoRequest.ReadDumpList(lDate)
            AnalyzeListDump.AnalizeDump(lDumpList)
        print u"done"

    @classmethod
    def AnalyzeBySpecailDate(cls, tDate):
        lDumpList = DumpInfoRequest.ReadDumpList(tDate)
        AnalyzeListDump.AnalizeDump(lDumpList)
        print u"done"

    @staticmethod
    def Test():
        lThis = MrgListDumpAnalyzer()
        lThis.AnalyzeByDateRange()
        # lDumpList = DumpInfoRequest.ReadDumpList(u"2018-01-26")
        # AnalyzeDump.AnalizeDump(lDumpList)




def GetSpecailDate(tDays,tFmt="%Y-%m-%d"):
    import datetime
    today = datetime.date.today()
    oneday = datetime.timedelta(days=tDays)
    iLastday = today - oneday
    return  iLastday.strftime(tFmt)




if __name__ == "__main__":
    # DumpInfoRequest.Test()

    # AnalyzeDump.Test()
    MrgListDumpAnalyzer.Test()
