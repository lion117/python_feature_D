# -*- coding: utf-8 -*-
"""
Created on 2014/8/21
@author: LEO
"""


from zipfile import *
import zipfile
import  os ,sys


def pyZipFile(tSrc):
    if os.path.isdir(tSrc)  is False:
        print  u'无效的文件夹路径' , tSrc
        raise  ValueError
        return False

    lExtList = ['.exp','.lib','.pdb','.zip','dmp']

    lDestFileName =os.path.join(os.getcwd(), 'FanXingReleasePkg.zip')
    if os.path.exists(lDestFileName):
        os.remove(lDestFileName)

    fzip = zipfile.ZipFile(lDestFileName, 'w', zipfile.ZIP_DEFLATED)

    lTotalFile = 0
    lZipFiles =0
    for dirpath,dirfilename, filenames in os.walk(tSrc, False):

        if HasTargetDir(dirpath):
            continue


        for itor in filenames:
            lTotalFile +=1
            if itor.find("PackageDir.exe") != -1:
                continue

            lExt = os.path.splitext(itor)[1]
            if lExt in lExtList :
                continue

            itemFileName =itor
            if dirpath != tSrc:
                itemFileName = dirpath[len(tSrc) + 1:] + '/' + itor
            i_file = os.path.join(dirpath, itor)
            try:
                print u"正在压缩第%d个文件\r"%lZipFiles,
                fzip.write(i_file, itemFileName)
                lZipFiles +=1
            except RuntimeError ,ex:
                print(ex)
                fzip.close()
                return False

    fzip.close()
    print (u"共有文件%d, 成功打包文件%d"%(lTotalFile,lZipFiles))
    lInput = raw_input()
    return  True



def HasTargetDir(tDir):
    lDir = tDir.replace("\\" ,"/")
    if lDir.find("/obj/")  != -1 or lDir.find("/lib/") !=-1:
        return  True
    else:
        return  False



def walkPath(t_path):
    print  t_path
    for (dirpath, dirnames, filenames) in os.walk(t_path):
        for filename in filenames:
            if '.idea' in dirpath:
                break
            if dirpath == t_path:
                print(os.path.join(dirpath, filename))  + "   "+ filename
            else:
                ext_folder = dirpath[len(t_path):]+ '/'
                print(os.path.join(dirpath, filename))  + "   "+ ext_folder+filename


gInfo = u'''
--------------------------------------------------------
使用说明：
1 将PackageDir.exe放置到release 目录下
2 点击运行
3 运行完成后,release目录项将生成一个FanXingReleasePkg.zip包
--------------------------------------------------------
'''


if __name__ == '__main__':
    # walkPath(os.getcwd())
    print gInfo
    pyZipFile(os.getcwd())




