# -*- coding: utf-8 -*-

from flask import Flask
from flask import redirect


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
    return  iLastday.strftime("%Y-%m-%d")


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=8081)
