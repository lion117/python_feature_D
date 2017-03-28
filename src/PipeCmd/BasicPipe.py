# -*- coding: utf-8 -*-



from subprocess import *
import threading
import time


gProjectName = "PD_103023_ELK"
gCmdLine = "start -branch  %s   -setVersion %s -uploadFtp -signature"




gProcess =Popen('compile.exe', shell=True, stdin=PIPE, stdout=PIPE)

def run():
    global gProcess
    while True:
        line = gProcess.stdout.readline()
        if not line:  #空则跳出
            break
        print(line.decode("GBK"))

    print("pipe is done ")   #跳出


def Main():
    w = threading.Thread(target=run)
    gProcess.stdin.write("3\r\n".encode("GBK"))
    # gProcess.stdin.flush()
    time.sleep(1)  # 延迟是因为等待一下线程就绪
    gProcess.stdin.write("list\r\n".encode("GBK"))
    # gProcess.stdin.flush()
    w.start()


def Test():
    global  gProjectName , gCmdLine, gProcess

    iThreadHandle = threading.Thread(target=run)
    iThreadHandle.start()
    time.sleep(1)  # 延迟是因为等待一下线程就绪
    gProcess.stdin.write("3\r\n".encode("GBK"))
    gProcess.stdin.flush()
    time.sleep(1)  # 延迟是因为等待一下线程就绪

    gProcess.stdin.write("clear\r\n".encode("GBK"))
    gProcess.stdin.flush()

    iIndex = 3
    while iIndex > 0:
        print("clear ing left %d seconds"%iIndex),
        iIndex -=1
        time.sleep(1)  # 延迟是因为等待一下线程就绪
        print "/r",

    iCmd = str.format(gCmdLine%(gProjectName , "9.9.9.9"))
    gProcess.stdin.write("%s\r\n"%iCmd)
    gProcess.stdin.flush()

    time.sleep(30)
#
#
# if __name__ == "__main__":
#     Main()


w =threading.Thread(target=run)
w.start()
gProcess.stdin.write("3\n")
gProcess.stdin.flush()
time.sleep(1) #延迟是因为等待一下线程就绪
gProcess.stdin.write("list\n")
gProcess.stdin.flush()
time.sleep(1)
