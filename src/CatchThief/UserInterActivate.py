# -*- coding: utf-8 -*-



import os, sys
import argparse
from GlobalCongif import *

def RunUserTerminator():
    # 创建参数解析器并解析参数
    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--area", type=int, default=150, help=u"分析的最小区域")
    ap.add_argument("-g","--gray",type=int, default=60,help=u"亮度提取灰度值")
    ap.add_argument("-n","--count",type=int, default=4,help=u"同时允许启动的处理视频进程数")
    ap.add_argument("-e","--effect",type=bool,default=False,help=u"是否使用直方图均衡化处理视频")
    ap.add_argument("-sd","--sourcedir",help=u"视频源文件夹路径,默认为软件启动当前文件夹下")
    ap.add_argument("-dd","--destdir",help=u"生成处理后的视频存储路径,默认与源路径相同")
    # ap.add_argument("-p","--process",help=u"启动独立的进程处理视频")
    ap.add_argument("-sf","--sourcefile",help=u"处理的视频源文件路径,需要配合'-p'才能使用")
    ap.add_argument("-df","--destfile",help=u"处理后存储的文件路径,需要配合'-p'才能使用")
    # ap.add_argument("-vf", "--video", help=u"分析视频文件的路径")
    args = vars(ap.parse_args())

    if args.get("sourcedir", None):
        g_sourceDir = args.get("sourcedir")
    else:
        g_sourceDir = os.getcwd()
    if args.get("destdir", None):
        g_destDir = args.get("destdir")
    else:
        g_destDir = os.getcwd()
    g_miniArea = args.get("area")
    g_grabValue = args.get("gray")
    g_bEffect = args.get("effect")

    if args.get("sourcefile",None)  and args.get("destfile",None) :
        print u"begin to dealing file %s"%(args.get("sourcefile"))
    else:
        pass

if __name__ == "__main__":
    RunUserTerminator()