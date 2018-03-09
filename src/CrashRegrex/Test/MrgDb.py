# -*- coding: utf-8 -*-

import sys, os, time



import sqlite3


class MrgCrashInfoDb():
    _dbName = u"crashinfo.db"
    def __init__(self):
        self._dbHandle = None
        self._dbHandle = self.CreatTable()

    def CreatTable(self):
           conn = sqlite3.connect(self._dbName)
           sql_create = u'''CREATE TABLE
                           IF NOT EXISTS tb_crashinfo_collect (
                            id INTEGER PRIMARY KEY ,
                            version   text NOT  NULL ,
                            crashdate  text NOT  NULL ,
                            modifydatetime text
                            )'''
           conn.execute(sql_create)
           conn.commit()
           return  conn


    def AddItemToDb(self,tVersion, tDate, tModify = None):
        if tModify is None:
            tModify =u""
        if self._dbHandle  is None:
            self._dbHandle = sqlite3.connect(self._dbName)
        sqlstr = unicode.format(u"INSERT INTO tb_crashinfo_collect (version,crashdate,modifydatetime) \
                      VALUES ('%s', '%s','%s' )" % (tVersion, tDate, tModify))
        self._dbHandle.execute(sqlstr)
        self._dbHandle.commit()




    def IsItemExist(self,tVersion,tDate):
        if self._dbHandle  is None:
            self._dbHandle = sqlite3.connect(self._dbName)
        cur = self._dbHandle.cursor()
        sqlstr = unicode.format(u"SELECT * FROM tb_crashinfo_collect WHERE version='%s' AND crashdate='%s'" %( tVersion, tDate))
        cur.execute(sqlstr)
        raws = cur.fetchall()
        lCount = len(raws)
        self._dbHandle.commit()
        if lCount > 0:
            return  True
        else:
            return  False

    def Release(self):
        if  self._dbHandle is not None:
            self._dbHandle.close()


    @staticmethod
    def Main():
        lMrgDb = MrgCrashInfoDb()
        lMrgDb.AddItemToDb(u"4.56.0.471" ,u"2018-01-25",u"2018-01-26")
        print lMrgDb.IsItemExist(u"4.56.0.470" ,u"2018-01-25")






if __name__ == "__main__":
    # ReadDb(u"")
    # AddItemToDb()
    MrgCrashInfoDb.Main()
    print os.getcwd()