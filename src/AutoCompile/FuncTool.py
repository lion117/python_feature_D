# -*- coding: utf-8 -*-



import os, sys
import re
import codecs



def GetVersion(tFile):
    with open(tFile, "r+") as f:
        rc_content = f.read()
        iStr = rc_content.decode('utf16')
        regex1 = re.compile(ur"VALUE\s*\"FileVersion\"\s*\,\s*\"\d+\.\d+\.\d+\.\d+\"", re.MULTILINE)
        regex2 = re.compile(ur"\d+\.\d+\.\d+\.\d+")
        iTemp = re.search(regex1, iStr)
        if iTemp is None:
            return  ""
        iTemp2 = re.search(regex2,iTemp.group())
        if iTemp2 is None:
            return  ""
        print iTemp2.group()
        return  iTemp2.group()


def GetSlnPath():
    pass


def SetRcVersion(tRcFile, TargetVersion):
    with open(tRcFile, "r+") as f:
        rc_content = f.read()
        iStr = rc_content.decode('GBK')
        regex1 = re.compile(ur"VALUE\s*\"FileVersion\"\s*\,\s*\"\d+\.\d+\.\d+\.\d+\"", re.MULTILINE)
        iTarget = unicode.format(u"VALUE  \"FileVersion\" , \"%s\""%TargetVersion)
        pass_2 = re.sub(regex1, iTarget, iStr,1)
        print pass_2
        if pass_2 is not  None:
            f.seek(0)
            f.write(pass_2.encode('GBK'))
            f.truncate()





def TestRc():
    iTarget = u"i am fine"
    iReplace = u'-'
    iRegex = re.compile(ur'\s')
    iResult = re.sub(iRegex,iReplace,iTarget)
    print iResult




if __name__ == "__main__":
    # GetVersion('./test.rc')
    SetRcVersion('./test.rc' ,'4.22.0.141')
    # TestRc()
    pass