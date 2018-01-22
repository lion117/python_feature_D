# -*- coding: utf-8 -*-

import sys, os, time


import socket
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


print get_ip_address()

if __name__ == "__main__":
    print os.getcwd()