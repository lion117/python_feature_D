# -*- coding: utf-8 -*-

import sys, os, time



import re


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
    if len(tList) == 0:
        return




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

    lReg = re.compile(ur"crash\d{1,3};count:\d{1,4};module:\w+;function:.*")
    lret = lReg.findall(tData,0,lPos)
    return lret


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
    lReg = re.compile(ur"\d{1,3} \w+, .*")
    lret = lReg.findall(tData, 0, lPos)
    return lret






if __name__ == "__main__":
    print os.getcwd()