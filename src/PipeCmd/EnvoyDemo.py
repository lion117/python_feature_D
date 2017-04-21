# -*- coding: utf-8 -*-



import os, sys
import time
import  envoy



if __name__ == "__main__":
    result = envoy.ConnectedCommand("ffmpeg.exe")
    print  result.send(str="ffmpeg -h")