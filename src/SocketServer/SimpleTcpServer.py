# -*- coding: utf-8 -*-



import os, sys
import time



from socket import *
from time import ctime
import  threading

HOST ='127.0.0.1'
PORT =  23058
PORT1 = 36484
PORT2 = 843
BUFSIZ = 1024



def run():
    ADDR = (HOST, PORT)
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)
    while True:
        print("waiting for a connection.....%d"%PORT)
        tcpCliSock, addr= tcpSerSock.accept()
        print("....connected from:", addr)

        while True:
            data = tcpCliSock.recv(BUFSIZ)
            print data
            # if not data:break
            # tcpCliSock.send(bytes('[%s] %s' % (ctime(), 'utf-8'), data))
        tcpCliSock.close()

def run2():
    ADDR = (HOST, PORT1)
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)
    while True:
        print("waiting for a connection.....%d"%PORT1)
        tcpCliSock, addr= tcpSerSock.accept()
        print("....connected from:", addr)

        while True:
            data = tcpCliSock.recv(BUFSIZ)
            print data
            # if not data:break
            # tcpCliSock.send(bytes('[%s] %s' % (ctime(), 'utf-8'), data))
        tcpCliSock.close()

def run3():
    ADDR = (HOST, PORT2)
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)
    while True:
        print("waiting for a connection.....%d"%PORT2)
        tcpCliSock, addr= tcpSerSock.accept()
        print("....connected from:", addr)

        while True:
            data = tcpCliSock.recv(BUFSIZ)
            print data
            # if not data:break
            # tcpCliSock.send(bytes('[%s] %s' % (ctime(), 'utf-8'), data))
        tcpCliSock.close()

def Test843():
    iThread843 = threading.Thread(target=run3)
    iThread843.start()

def TestComm():
    iThread = threading.Thread(target=run)
    iThread.start()
    run2()

def TestAll():
    iThread843 = threading.Thread(target=run3)
    iThread843.start()
    time.sleep(0.1)
    iThread = threading.Thread(target=run)
    iThread.start()
    run2()


def UserInterActivate():
    iHelp =u'''请输入命令：
    1. 占用通信端口
    2. 占用flash端口
    3. 占用以上所有端口
    '''
    while(True):
        print(iHelp)
        iIndex = raw_input()
        if iIndex == '1':
            TestComm()
        elif iIndex == '2':
            Test843()
        elif iIndex == '3':
            TestAll()
        else:
            print u"用户输入错误,请输入[1,3]之间的数值"




if __name__ == "__main__":
    UserInterActivate()
