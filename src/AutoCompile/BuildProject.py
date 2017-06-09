# -*- coding: utf-8 -*-



import os, sys
import time
import subprocess as sbp
import RegLocation
import ParaConfig


def BuildSln():
    iBuildTool = RegLocation.GetVS14ToolPath()
    sbp.call([iBuildTool, ParaConfig.g_projectPath, "/rebuild", "release"])


def GitPull(tGitUrl, tGitBrach, tDesDir):
    sbp.call(["C:\\Program Files\\Git\\bin\\git.exe", "clone", "--progress", "--branch", tGitBrach, "-v", tGitUrl, tDesDir])


if __name__ == "__main__":
    # BuildSln()
    GitPull("git@git.oschina.net:leocode/TestScriptBuildVsProject.git","master",os.getcwd()+"/GitDir")
