# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""       turtle-example-suite:

            tdemo_yinyang.py

Another drawing suitable as a beginner's
programming example.

The small circles are drawn by the 畫圓
command.

"""

from turtle_tc_01 import *

def 陰陽(半徑長, 顏色1, 顏色2):
    筆寬(3)
    顏色(黑, 顏色1)
    開始填()
    畫圓(半徑長/2., 180)
    畫圓(半徑長, 180)
    左轉(180)
    畫圓(-半徑長/2., 180)
    結束填()
    左轉(90)
    提筆()
    前進(半徑長*0.35)
    右轉(90)
    下筆()
    顏色(顏色1, 顏色2)
    開始填()
    畫圓(半徑長*0.15)
    結束填()
    左轉(90)
    提筆()
    後退(半徑長*0.35)
    下筆()
    左轉(90)

def 主函數():
    重設()
    陰陽(200, 黑, 白)
    陰陽(200, 白, 黑)
    藏龜()
    return "結束!"

if __name__ == '__main__':
    主函數()
    主迴圈()
