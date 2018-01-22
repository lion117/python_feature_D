# -*- coding: utf-8 -*-

from flask import Flask
from flask import redirect
import ctypes

app = Flask(__name__)
gIndex = 0

@app.route('/',methods=['GET','POST'])
def Index():
    lUrl = "http://dumpupload.fanxing.com/fxlist.php?date=%s&format=link"%GetLastday()
    return  redirect(lUrl)




def GetLastday(tDays= 1):
    import datetime
    today = datetime.date.today()
    oneday = datetime.timedelta(days=tDays)
    iLastday = today - oneday
    # iStrYesterday = time.strftime("%y%m%d",iLastday)
    return  iLastday.strftime("%Y-%m-%d")


def HideWnd():
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)



if __name__ == '__main__':
    HideWnd()
    app.run(host="0.0.0.0",debug=True,port=80)
