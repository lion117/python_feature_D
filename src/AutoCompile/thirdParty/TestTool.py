# -*- coding: utf-8 -*-



import os, sys
import time

if __name__ == "__main__":
    import subprocess as sbp
    try:
        sbp.call(["C:\\Windows\\System32\\quser.exe"])
    except Exception ,ex:
        print ex