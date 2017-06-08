# -*- coding: utf-8 -*-

import _winreg

def GetVS12ToolPath():
    key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,                     r"SOFTWARE\Wow6432Node\Microsoft\VisualStudio\12.0")
    value,type = _winreg.QueryValueEx(key,"InstallDir")
    iTool = unicode(value) + u"devenv.com"
    return  iTool


def GetVS14ToolPath():
    key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,                     r"SOFTWARE\Wow6432Node\Microsoft\VisualStudio\14.0")
    value,type = _winreg.QueryValueEx(key,"InstallDir")
    iTool = unicode(value) + u"devenv.com"
    return  iTool

def GetNsisPath():
    key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Wow6432Node\NSIS")
    value,type = _winreg.QueryValueEx(key,"")
    iTool = unicode(value) + u"makensis.exe"
    return  iTool


if __name__ == "__main__":
    print  GetVS12ToolPath()
    print  GetVS14ToolPath()
    print GetNsisPath()
