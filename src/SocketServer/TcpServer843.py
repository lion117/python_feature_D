# -*- coding: utf-8 -*-




from socket import *
from time import ctime
import  threading

HOST ='127.0.0.1'
PORT = 843
PORT1 = 23058
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


iThread = threading.Thread(target=run)
iThread.start()
