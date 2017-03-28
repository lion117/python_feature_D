# -*- coding: utf-8 -*-



import os, sys
import time
import sqlite3



def main():
    conn = sqlite3.connect('songlist.db')
    try:



        iCursor = conn.cursor()
        iCursor.execute("DELETE  FROM SongList_2")
        conn.commit()

        print "once time head: " + time.asctime(time.localtime(time.time()))
        for i in range(500):
            iSql = str.format(
                "insert into SongList_2 values (NULL, 'A5F865B4A0E8CFE9E8BA5BDDB8A83C71%d', '张学友 - 情网.mp3', '张学友 - 情网', 0, ' ', 'D:\System\Document\FXbanzou\Buffer\Beyond - 光辉岁月.mp3', ' ', 1, 123456789, 3456789, 456789, 789456)" % i)
            # ===================================
            iCursor.execute(iSql)
        conn.commit()
        print  "once time tail: " + time.asctime(time.localtime(time.time()))

        # print "comp time head: " + time.asctime(time.localtime(time.time()))
        # iAllSql=""
        # for i in range(500):
        #     iSql = str.format(
        #         "insert into SongList_2 values (NULL, 'A5F865B4A0E8CFE9E8BA5BDDB8A83C71%d', '张学友 - 情网.mp3', '张学友 - 情网', 0, ' ', 'D:\System\Document\FXbanzou\Buffer\Beyond - 光辉岁月.mp3', ' ', 1, 123456789, 3456789, 456789, 789456)" % i)
        #     if iAllSql is None:
        #         iAllSql = iSql
        #     else:
        #         iAllSql += "; "+ iSql
        #     # ===================================
        #
        # iCursor.execute(iAllSql)
        # conn.commit()
        # print  "comp time tail: " + time.asctime(time.localtime(time.time()))


        # print "each time head: "+ time.asctime( time.localtime(time.time()) )
        # for i in range(500):
        #     iSql = str.format("insert into SongList_2 values (NULL, 'A5F865B4A0E8CFE9E8BA5BDDB8A83C71%d', '张学友 - 情网.mp3', '张学友 - 情网', 0, ' ', 'D:\System\Document\FXbanzou\Buffer\Beyond - 光辉岁月.mp3', ' ', 1, 123456789, 3456789, 456789, 789456)"%i)
        #     # ===================================
        #     iCursor.execute(iSql)
        #     conn.commit()
        # print "each time tail: " + time.asctime( time.localtime(time.time()) )







    except Exception , ex:
            print ex


    pass


if __name__ == "__main__":
    main()