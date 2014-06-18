# -*- coding: utf-8 -*-
# colormixer


from turtle_tc import * #NEW
import sys
sys.setrecursionlimit(20000)   # overcomes, for now, an instability of Python 3.0

class 顏色龜(龜類):

    def __init__(我, x, y):
        龜類.__init__(我)
        我.形狀(龜形)
        我.重設大小模式("user")
        我.形狀大小(3,3,5)
        我.筆粗(10)
        我._color = [0,0,0]
        我.x = x
        我._color[x] = y
        我.顏色(我._color)
        我.速度(0)
        我.左轉(90)
        我.提筆()
        我.前往(x,0)
        我.下筆()
        我.設y座標(1)
        我.提筆()
        我.設y座標(y)
        我.筆色("gray25")
        我.在拖曳時(我.移動)

    def 移動(我, x, y):
        我.設y座標(max(0,min(y,1)))
        我._color[我.x] = 我.y座標()
        我.填色(我._color)
        設背景顏色()

def 設背景顏色():
    螢幕.背景色(紅龜.y座標(), 綠龜.y座標(), 藍龜.y座標())

def main():
    global 螢幕, 紅龜, 綠龜, 藍龜
    螢幕  = 幕類()
    螢幕.延遲(0)
    螢幕.設座標系統(-1, -0.3, 3, 1.3)

    紅龜 = 顏色龜(0, .5)
    綠龜 = 顏色龜(1, .5)
    藍龜 = 顏色龜(2, .5)
    設背景顏色()

    寫字龜 = 龜類()
    寫字龜.藏龜()
    寫字龜.提筆()
    寫字龜.前往(1,1.15)
    寫字龜.寫("拖拉(DRAG)!",align="center",font=("Arial",30,("bold","italic")))
    return "事件迴圈"

if __name__ == "__main__":
    msg = main()
    印(msg)
    主迴圈()
