# -*- coding: utf-8 -*-



import SocketServer
from SocketServer import StreamRequestHandler as SRH
from time import ctime

host = '127.0.0.1'
port_flash = "843"
port_comm1= "36484"
port_comm2 = "23058"
addr_flash = (host,port_flash)
addr_comm1 = (host,port_comm1)
addr_coom2 = (host,port_comm2)

class Servers(SRH):
    def handle(self):
        print 'got connection from ',self.client_address
        self.wfile.write('connection %s:%s at %s succeed!' % (host,port,ctime()))
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            print data
            print "RECV from ", self.client_address[0]
            self.request.send(data)





if __name__ == "__main__":
    print 'server is running....'
    server = SocketServer.ThreadingTCPServer(addr_flash,Servers)
    server.serve_forever()
