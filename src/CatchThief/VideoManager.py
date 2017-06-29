# -*- coding: utf-8 -*-



import os, sys
import subprocess as subp
import threading



def WalkTargetFiles(tDir, tExt):
    iList = []
    for (dirpath, dirnames, filenames) in os.walk(tDir):
        for itorFile in filenames:
            if os.path.splitext(itorFile)[1] == tExt:
                iList.append(itorFile)
    return iList

def SetupProcess(tFile):
    subp.call(["C:\\Python27\\python.exe","Multi_CatchThief.py","-v",tFile])


def BatchRename(tDir, tFormat):
    lList = WalkTargetFiles(tDir, ".png")
    lList.sort(key= str.lower)
    iCount = len(lList)
    for itor in range(iCount):
        lStrName = str.format(tFormat%itor)
        os.rename(lList[itor],lStrName)


def Run():
    iList = WalkTargetFiles(os.getcwd(), '.mp4')
    for itor in iList:
        print u"Setup Process filename :%s"%itor
        lThread =threading.Thread(target=SetupProcess,args=(itor,))
        lThread.start()



if __name__ == "__main__":
    # Run()
    # BatchRename(os.getcwd(),"face_in_%04d.png")
    pass



