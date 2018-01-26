# -*- coding: utf-8 -*-

import sys, os, time
import requests

import MrgVerCfg
from  PyUtils import HttpDonwload , GetLastday
from tqdm import tqdm
import PyUtils


gUrl = u"http://dumpupload.fanxing.com/fxlist.php?date=%s&format=json"%GetLastday(tFmt="%Y-%m-%d")
gVer=u"4.50.0.420"






def ParseFiles(url):
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


def GenerateFilter(tType,tVer= None):
    if tType == 0:
        lFilter = unicode.format(u"Partner_CrashDump_V%s"%tVer)
        return lFilter
    elif tType == 1:
        return None
    else:
        return None



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



def DownloadDump(tVer, tData, tDir = None):
    lUrl = u"http://dumpupload.fanxing.com/fxlist.php?date=%s&format=json"%tData
    lList = ParseFiles(gUrl)
    lList = Filter(lList, GenerateFilter(0, tVer))
    for itor in tqdm(lList):
        HttpDonwload(itor, tDir)
    print (u"下载完成")
    PyUtils.OpenDir(tDir)
    MrgVerCfg.SetVersion(tVer)



def Main():
    lList = ParseFiles(gUrl)
    lList = Filter(lList,GenerateFilter(0,gVer))
    for itor in tqdm(lList):
        HttpDonwload(itor, os.path.join(os.getcwd(),GetLastday(tFmt="%Y-%m-%d")))
    print (u"done")


if __name__ == "__main__":
    Main()
