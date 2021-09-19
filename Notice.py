# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:08:29 2020

@author: McLaren
"""
import telebot
import Global_Config
# 请使用TG机器人进行消息推送
# 详情谷歌
TOKEN = ''
CHATID = ''

def sent_message(text='system error'):
    if Global_Config.isPushMsg:
        tb = telebot.TeleBot(TOKEN)
        tb.send_message(CHATID, text)

# import telebot
# 测试
# TOKEN = ''
# CHATID = ''

# def sent_message(text='system error'):
#     if True:
#         tb = telebot.TeleBot(TOKEN)
#         tb.send_message(CHATID, text)

# sent_message()