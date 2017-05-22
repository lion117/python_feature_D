# -*- coding: utf-8 -*-



import os, sys
import time



from socket import *
from time import ctime
import  threading

HOST ='127.0.0.1'
PORT = 36484
PORT1 = 23058
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
            if not data:break
            tcpCliSock.send(bytes('[%s] %s' % (ctime(), 'utf-8'), data))
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
            if not data:break
            tcpCliSock.send(bytes('[%s] %s' % (ctime(), 'utf-8'), data))
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
            if not data:break
            tcpCliSock.send(bytes('[%s] %s' % (ctime(), 'utf-8'), data))
        tcpCliSock.close()

iThread843 = threading.Thread(target=run3)
iThread843.start()
time.sleep(0.1)
iThread = threading.Thread(target=run)
iThread.start()
run2()


