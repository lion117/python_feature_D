# -*- coding: utf-8 -*-



import os, sys
import time

def PrintTime():
    for _ in range(11):
        print "\r",
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        time.sleep(1)


if __name__ == "__main__":
    PrintTime()