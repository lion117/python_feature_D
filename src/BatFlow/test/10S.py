# -*- coding: utf-8 -*-



import os, sys
import time


def waitFor10S():
    for i in range(11):
        print "\r",
        print "index : %d "%i,
        time.sleep(1)


if __name__ == "__main__":
    waitFor10S()
