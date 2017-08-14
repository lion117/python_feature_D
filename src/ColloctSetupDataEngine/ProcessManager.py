# -*- coding: utf-8 -*-



import os, sys
import time
import  subprocess as sbp
import CollectData
import win32gui
import psutil


g_path = u"D:\\360极速浏览器下载\\酷狗直播伴侣\\FanXingBanZou.exe"


def SetupFxProcess(tFileName):
    if os.path.exists(tFileName):
        strFile = tFileName.encode('gbk')
        pObject =sbp.Popen([strFile,"startup"])
        return pObject.pid
    else:
        return  0


def IsWndExist():
    classname = "FanXingPartner"
    titlename = "酷狗直播伴侣"
    hwnd = win32gui.FindWindow(classname, None)
    return  hwnd

def KillProcess(tPid):
    # os.system("taskkill /PID %d"%tPid)
    p = psutil.Process(tPid)
    p.terminate()  #or p.kill()


def killFxProcess():
    for proc in psutil.process_iter():
        try:
            if proc.name() == "FanXingPartner.exe" or proc.name() == "FanXingBanZou.exe" or proc.name() == "FxbzUpdate.exe":
                print ("target process id : %d , process name : %s  have been killed" % (proc.pid, proc.name()))
                proc.kill()
        except psutil.AccessDenied, ex:
            # print(str(ex))
            pass






class ColloctSetupDataEngine():
    def __init__(self, tTimes):
        self._setupTimes = tTimes

    def CleanEnv(self):
        hwnd = IsWndExist()
        killFxProcess()
        print u"clean fanxingbanzou process clean"
        time.sleep(1)
        lLog = CollectData.GetFxLogPath()
        if os.path.exists(lLog):
            os.remove(lLog)
            print u"clean log"



    def RunTask(self):
        self.CleanEnv()
        print u"begin to setup software for %d times"%self._setupTimes
        while(self._setupTimes> 0):
            print u"setup process %d"%self._setupTimes
            pid = SetupFxProcess(g_path)
            if pid == 0:
                print u"setup process failed , software exist"
                break
            else:
                time.sleep(3)
                while(IsWndExist() is None):
                    time.sleep(1)
                KillProcess(pid)
                self._setupTimes -= 1
                while(IsWndExist()):
                    time.sleep(1)

        CollectData.AnalyzeLog()





if __name__ == "__main__":
    # print(os.path.abspath("__file__"))
    # print(os.getcwd())
    # pid =  SetupFxProcess(g_path)
    # print pid
    # if IsWndExist():
    #     print 'find'
    # else:
    #     print 'not find'
    # time.sleep(2)
    # KillProcess(pid)
    lEngin = ColloctSetupDataEngine(20)
    lEngin.RunTask()
    pass