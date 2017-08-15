# -*- coding: utf-8 -*-



import os, sys
import time
import re
import csv
import datetime
import platform

def FilterTimeList(tFileName):
    with open(tFileName) as lFile:
        lBuff = lFile.read()
        lContext = lBuff.decode("GBK")
        lCompile = re.compile(ur"\[delay time\]\sonshowwindow:\s\d*")
        lGroup = lCompile.findall(lContext)
        lList = []
        for itor in lGroup:
            lNumb = re.findall(ur"\d+", itor)
            if lNumb :
                lList.append(lNumb[0])
        return  lList

def WriteData(tList):
    lAvarange = GetAverage(tList)
    print u"共有数据 %d 项, 平均启动时长为  %d"%(len(tList), lAvarange)
    lFileName = str.format("%0.2fms_%dCounts_%s_%s.csv"%(GetAverage(tList),len(tList), GetDataTime(),platform.platform()))
    header = ['time']
    with open(lFileName,'wb') as f:
        f_csv = csv.writer(f, header)
        # f_csv.writeheader()
        # for itor in tList:
        f_csv.writerow(tList)


def GetAverage(tList):
    lSum = 0
    try :
        for itor in tList:
            lSum += float(itor)
    except Exception,ex:
        print ex
        return  0
    if len(tList) is 0:
        return  0
    return  float(lSum)/len(tList)

def GetDataTime():
    ltoday = datetime.datetime.today()
    lstr = ltoday.strftime('%Y%m%d-%H%M%S')
    return  lstr


def AnalyzeLog():
    lLogFile = GetFxLogPath()
    lList = FilterTimeList(lLogFile)
    WriteData(lList)



def GetFxLogPath():
    appdata = os.getenv("APPDATA")
    lLog = os.path.join(appdata,"FXbanzou/log.txt")
    return  lLog


def test_writer():
  # csv文件必须以二进制方式open
  with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow([u'Spam', u'Lovely Spam', u'Wonderful Spam'])


if __name__ == "__main__":
    # lList = FilterTimeList("log.txt")
    # WriteData(lList)
    # print  GetDataTime()
    AnalyzeLog()
    # print platform.version()