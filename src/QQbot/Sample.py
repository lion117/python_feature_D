# -*- coding: utf-8 -*-

import sys, os, time


def onQQMessage(bot, contact, member, content):
    if content == '-hello':
        bot.SendTo(contact, '你好，我是QQ机器人')
    elif content == '-stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()



if __name__ == "__main__":
    print os.getcwd()