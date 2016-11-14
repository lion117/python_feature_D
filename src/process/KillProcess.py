# -*- coding: utf-8 -*-



import os, subprocess
import time
import  psutil


def killFxProcess():
    for proc in psutil.process_iter():
           try:
               if proc.name() == "FanXingPartner.exe":
                   print ("target process id : %d , process name : %s  have been killed"% (proc.pid, proc.name()) )
                   proc.kill()
           except psutil.AccessDenied, ex:
               print(str(ex) )



def test():
    for proc in psutil.process_iter():
        try:
            if proc.name() == "FanXingPartner.exe":
                print ("target process id : %d , process name : %s  have been killed"% (proc.pid, proc.name()) )
                proc.kill()
        except psutil.AccessDenied, ex:
            print(str(ex) )
    # pids = psutil.pids()
    # for pid in pids:
    #     p = psutil.Process(pid)
    #     print  p.name()
        # i_count =0
        # if p.name() == u"FanXingPartner.exe":
        #     print  pid
        #     i_count +=1
        #     print  i_count



if __name__ == "__main__":
    killFxProcess()