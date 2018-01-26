# -*- coding: utf-8 -*-

import sys, os, time
import requests



def HttpDonwload(tUrl, tDir= None):
    if tUrl is None:
        return  False
    lBaseName = tUrl.split('/')[-1]
    if tDir is None:
        lFileName = os.path.join(os.getcwd(),lBaseName)
    else:
        if os.path.exists(tDir) == False:  # 判断本地是否有该文件目录，如果没有，将创建
            os.mkdir(tDir)
        lFileName = os.path.join(tDir,lBaseName)
    r = requests.get(tUrl, stream=True)
    with open(lFileName, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()  # commented by recommendation from J.F.Sebastian
    return True




def GetLastday(tDays= 1,tFmt="%Y%m%d"):
    import datetime
    today = datetime.date.today()
    oneday = datetime.timedelta(days=tDays)
    iLastday = today - oneday
    return  iLastday.strftime(tFmt)


def GetToday(tFmt="%Y%m%d"):
    import datetime
    today = datetime.date.today()
    return str.format(tFmt%(today.year,today.month,today.day))



def OpenDir(filename):
  try:
    os.startfile(filename)
  except:
    import subprocess
    subprocess.Popen(['xdg-open', filename])




if __name__ == "__main__":
    print os.getcwd()