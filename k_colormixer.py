# -*- coding: utf-8 -*-
# colormixer


from turtle_tc_01 import * #NEW
import sys
sys.setrecursionlimit(20000)   # overcomes, for now, an instability of Python 3.0

class 顏色龜(龜類):

    def __init__(self, x, y):
        龜類.__init__(self)
        self.形狀(龜形)
        self.重設大小模式("user")
        self.形狀大小(3,3,5)
        self.筆粗(10)
        self._color = [0,0,0]
        self.x = x
        self._color[x] = y
        self.顏色(self._color)
        self.速度(0)
        self.左轉(90)
        self.提筆()
        self.前往(x,0)
        self.下筆()
        self.設y座標(1)
        self.提筆()
        self.設y座標(y)
        self.筆色("gray25")
        self.在拖曳時(self.移動)

    def 移動(self, x, y):
        self.設y座標(max(0,min(y,1)))
        self._color[self.x] = self.y座標()
        self.填色(self._color)
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

    writer = 龜類()
    writer.藏龜()
    writer.提筆()
    writer.前往(1,1.15)
    writer.寫("拖拉(DRAG)!",align="center",font=("Arial",30,("bold","italic")))
    return "事件迴圈"

if __name__ == "__main__":
    msg = main()
    印(msg)
    主迴圈()
