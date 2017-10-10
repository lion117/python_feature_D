# -*- coding: utf-8 -*-

import  sys, os,time

import xlwt


def WriteData():
    data=xlwt.Workbook()
    table=data.add_sheet('name')
    table.write(0,0,u'呵呵')
    table.write(1,0,u'呵呵')
    table.write(2,0,u'呵呵')
    data.save('test.xls')



def WalkDirFiles(tDir):
    iDict = {}
    for (dirpath, dirnames, filenames) in os.walk(tDir):
        for itorFile in filenames:
            if itorFile.find('_mix.pcm') != -1:   # only mix file accept
                lDir = os.path.relpath(dirpath)
                if lDir is '.':
                    continue  # skip current dir
                if iDict.has_key(lDir) is False:
                        iDict[lDir] = []
                iList = iDict[lDir]
                iList.append(itorFile)
    return  iDict


def WriteExcelData(tDict):
    lExcel = xlwt.Workbook()
    for lSheet in tDict.keys():
        table = lExcel.add_sheet(lSheet)
        table.write(0, 0, u'文件名')
        table.write(0, 1, u'问题点')
        lList = tDict[lSheet]
        lIndex = 1
        for itorFile in lList:
            table.write(lIndex, 0, itorFile)
            table.write(lIndex, 1, ParseFileName(itorFile))
            lIndex +=1
    if len(tDict) ==0:
        print u"not data to save excel"
        return
    lExcel.save(u'主播真唱数据.xls')

def ParseFileName(tFileName):
    if tFileName.find('nRet0') != -1:
        return  u"不唱歌"
    elif tFileName.find('nRet1') != -1:
        return  u"唱歌"
    else:
        return  u"未知错误"



if __name__ == "__main__":
    lDict = WalkDirFiles(os.getcwd())
    WriteExcelData(lDict)