#!python3
#coding:utf8

import win32api
import win32con
import win32gui
#  基本操作win窗口显示
win32api.MessageBox(None,"Hello,pywin32!","pywin32",win32con.MB_OK)