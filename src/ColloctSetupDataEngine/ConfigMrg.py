# -*- coding: utf-8 -*-



import os, sys
import time
import ConfigParser

g_exeFile = u"C:\\Program Files (x86)\\FanXingBanZou\\FxbzUpdate.exe"
g_Times = 20


def ReadConfig():
    global g_exeFile,g_Times
    lCfgFile = u"config.ini"
    if os.path.exists(lCfgFile) is False:
        print("config file is not exist , use default value")
        try:
            lCfg = ConfigParser.ConfigParser()
            lCfg.read("config.ini")
            if lCfg.has_section("info") is False:
                lCfg.add_section("info")
            lCfg.set("info","exe",g_exeFile.encode("gbk"))
            lCfg.set("info","times",g_Times)
            lCfg.write(open("config.ini", "w"))
        except Exception,exinfo:
            print exinfo
        return (g_exeFile, g_Times)
    try:
        lCfg = ConfigParser.ConfigParser()
        lCfg.read(lCfgFile)
        g_exeFile = lCfg.get("info","exe")
        g_exeFile = g_exeFile.decode("gbk")
        g_Times = lCfg.getint("info","times")
        return (g_exeFile, g_Times)
    except Exception,exinfo:
        print exinfo
        return (g_exeFile, g_Times)







if __name__ == "__main__":

    print ReadConfig()