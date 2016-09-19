# -*- coding: utf-8 -*-



import os, sys
import time

g_ext = ['jpg','jpeg','gif','png','bmp']


def walkFiles(t_path):
    i_file_list = []
    for (dirpath, dirnames, filenames) in os.walk(t_path):
        for filename in filenames:
            i_ext = os.path.splitext(filename)[1][1:]
            if i_ext in g_ext:
                i_file_list.append(os.path.join(dirpath, filename))
    return i_file_list


def deleFiles(t_list):
    for itor in t_list:
        print(str(itor))
        os.remove(itor)



if __name__ == "__main__":
    print(u"删除的文件格式有： " + unicode(g_ext))
    deleFiles(walkFiles(os.getcwd()))