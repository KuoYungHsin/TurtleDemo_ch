# -*- coding: utf-8 -*-
#!/usr/bin/env python3
## DEMONSTRATES USE OF 2 CANVASES, SO CANNOT BE RUN IN DEMOVIEWER!
"""turtle example: Using 龜幕類 and 原生龜類
for drawing on two distinct canvases.
"""
import tkinter as TK
from turtle_tc_01 import *    #new
root = TK.Tk()
畫布1 = TK.Canvas(root, width=300, height=200, bg="#ddffff") #筆寬=>width
畫布2 = TK.Canvas(root, width=300, height=200, bg="#ffeeee")
畫布1.pack()
畫布2.pack()

s1 = 龜幕類(畫布1)
s1.背景色(0.85, 0.85, 1)
s2 = 龜幕類(畫布2)
s2.背景色(1, 0.85, 0.85)

紅龜 = 原生龜類(s1)
藍龜 = 原生龜類(s2)

紅龜.顏色(紅, (1, 0.85, 0.85))
紅龜.筆寬(3)
藍龜.顏色(藍, (0.85, 0.85, 1))
藍龜.筆寬(3)

for t in 紅龜,藍龜:
    t.形狀(龜形)
    t.左轉(36)

藍龜.左轉(180)

for t in 紅龜, 藍龜:
    t.開始填()
for i in 範圍(5):
    for t in 紅龜, 藍龜:
        t.前進(50)
        t.左轉(72)
for t in 紅龜,藍龜:
    t.結束填()
    t.左轉(54)
    t.提筆()
    t.後退(50)

## Want to get some info?

#印(s1, s2)
#印(p, q)
#印(s1.龜群())
#印(s2.龜群())

TK.mainloop()   #主迴圈=>mainloop
