# -*- coding: utf-8 -*-
import time
import os, sys
import flask
import grin

from flask import Flask
from flask import redirect,url_for,request , make_response


app = Flask(__name__)
gIndex = 0

@app.route('/',methods=['GET','POST'])
def Index():
    # print request.headers
    global  gIndex
    print "recive data from client %d"%gIndex
    gIndex +=1
    print request.data
    return  "POST ok"
    # if request.method == "POST":
    #     print "POST method"
    #     return "OK"
    # elif request.method == "GET":
    #     print "GET method"
    #     return  "GET"


@app.route('/api',methods=['GET','POST'])
def API():
    print "ShowLove"
    if request.method == "POST":
        print request.form.__sizeof__()
        print request.form["group"]
        print "POST method"
        return "OK"
    elif request.method == "GET":
        print "GET method"
        return  "GET"


if __name__ == '__main__':
    app.run(host="172.17.1.110",debug=True,port=80)
