# -*- coding: utf-8 -*-

import sys, os, time
import PyUtils
import MrgDb
import AnalizeCrashList


class MrgCrashInfo():


    @classmethod
    def run(cls):
        ldb = MrgDb.MrgCrashInfoDb()
        while True:
            lDate = PyUtils.GetLastday(1, '%Y-%m-%d')
            if ldb.IsItemExist(lDate):
                 time.sleep(10)
            else:
                AnalizeCrashList.MrgListDumpAnalyzer.AnalyzeBySpecailDate(tDate = lDate)
                ldb.AddItemToDb(u"",lDate)
                print u"finish date:%s  analyze "



    @staticmethod
    def main():
        pass




if __name__ == "__main__":
    print os.getcwd()