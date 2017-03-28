# -*- coding: utf-8 -*-



# from subprocess import *
# import threading
import time
import  subprocess
import tornado.process

gProjectName = "PD_103023_ELK"
gVersion="6.6.6.6"





gCmdLine = "start -branch  %s   -setVersion %s -uploadFtp -signature\n"





# gProcess = subprocess.Popen('ffmpeg.exe', bufsize=10240, shell=True,stdin=subprocess.PIPE , stdout=subprocess.PIPE)
# # print  gProcess.communicate()
# time.sleep(1)


def Demo1():
    subprocess.call("ffmpeg -i 1.flv")
    time.sleep(2)
    subprocess.call("ffmpeg -h")


def Demo2():
    iP1 = subprocess.Popen(['cmd.exe'], bufsize=10240, shell=True,stdin=subprocess.PIPE , stdout=subprocess.PIPE)
    iP2 = subprocess.Popen(['ping','baidu.com'], bufsize=10240, shell=True,stdin=iP1.stdout , stdout=subprocess.PIPE)
    print iP2.stdout.read()


def Demo3():
    iP1 = subprocess.Popen(['compile.exe'], bufsize=1024, shell=True,stdin=subprocess.PIPE , stdout=subprocess.PIPE)
    print iP1.stdout.read()
    time.sleep(2)
    iP2 = subprocess.Popen(['3\n'], bufsize=1024, shell=True,stdin=iP1.stdout , stdout=subprocess.PIPE)
    print iP2.stdout.read()
    iP3 = subprocess.Popen(['list\n'], bufsize=1024, shell=True,stdin=iP2.stdout , stdout=subprocess.PIPE)

def Demo4():
    iP1 = subprocess.Popen(['compile.exe'], bufsize=1024, shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE )
    iP1.stdin.write("3\n")
    iP1.stdin.flush()
    time.sleep(1)
    iP1.stdin.write("list\n")
    iP1.stdin.flush()
    print iP1.stdout.read()





if __name__ == "__main__":

    Demo4()
    # print iResult[1]
    # print gProcess.stdout.read()
    # time.sleep(2)
    # gProcess.stdin.write("ffmpeg -i 1.flv\n")
    # gProcess.stdin.flush()
    # time.sleep(1) #延迟是因为等待一下线程就绪
    # gProcess.stdin.write("ffmpeg -i 1.flv\n")
    # gProcess.stdin.flush()
    # time.sleep(1)
    # gProcess.stdin.write("clear\n")
    # gProcess.stdin.flush()
    # iIndex = 0
    # print "waiting for clean ... %d"%iIndex,
    # while iIndex < 3:
    #     print "\rwaiting for clean ... %d"%iIndex,
    #     iIndex+=1
    #     time.sleep(1)
    # print "\rbegin to compile project"
    # gCmdLine = str.format(gCmdLine%(gProjectName,gVersion))
    # gProcess.stdin.write(gCmdLine)
    # gProcess.stdin.flush()
    iInput = raw_input()
