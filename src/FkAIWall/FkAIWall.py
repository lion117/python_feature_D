# -*- coding: utf-8 -*-

import sys, os, time
import urllib2
import  random


def VisitWeb():
    url="http://hesiyuan.vip/dump"
    try:
        lTimeOut = random.randint(3,4)
        content=urllib2.urlopen(url, timeout=lTimeOut)
        print content
    except Exception ,ex:
        print ex


def MgrVisitWeb():
    lIndex =  0
    while(True):
        lTimeOut = random.randint(9,30)
        time.sleep(lTimeOut)
        lIndex +=1
        print u" visit web %d" % lIndex
        VisitWeb()


def Run():
    # setup exe

    # setup server
    MgrVisitWeb()


if __name__ == "__main__":
    print os.getcwd()
    Run()