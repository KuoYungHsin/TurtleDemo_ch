# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""       turtle-example-suite:

            tdemo_paint.py

A simple  eventdriven paint program

- use 左轉 mouse button to move turtle
- middle mouse button to change 顏色
- 右轉 mouse button do turn 是否正在填色 on/off
 -------------------------------------------
 Play around by clicking into the canvas
 using all three mouse buttons.
 -------------------------------------------
          To exit press STOP button
 -------------------------------------------
"""
from turtle_tc import *

def  下筆切換(x=0, y=0):
    if 筆()["pendown"]:
        結束填()
        提筆()
    else:
        下筆()
        開始填()

def 換顏色(x=0, y=0):
    global 顏色表
    顏色表 = 顏色表[1:]+顏色表[:1]
    顏色(顏色表[0])

def 主函數():
    global 顏色表
    形狀("circle")
    重設大小模式("user")
    形狀大小(.5)
    筆寬(3)
    顏色表=[紅, 綠, 藍, 黃]
    顏色(顏色表[0])
    下筆切換()
    在點擊幕時(前往,1)
    在點擊幕時(換顏色,2)
    在點擊幕時(下筆切換,3)
    return "EVENTLOOP"

if __name__ == "__main__":
    訊息  = 主函數()
    印(訊息 )
    主迴圈()
