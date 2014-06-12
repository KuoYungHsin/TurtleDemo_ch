# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""       turtle-example-suite:

            tdemo_yinyang.py

Another drawing suitable as a beginner's
programming example.

The small circles are drawn by the 畫圓
command.

"""

from turtle_jp import *

def 陰陽(半径の長さ, 色1, 色2):
    ペン幅(3)
    カラー(黑, 色1)
    塗りつぶ_開始()
    畫圓(半径の長さ/2., 180)
    畫圓(半径の長さ, 180)
    左(180)
    畫圓(-半径の長さ/2., 180)
    塗りつぶ_終わり()
    左(90)
    アップ_ペン()
    進める(半径の長さ*0.35)
    右折(90)
    ダウン_ペン()
    カラー(色1, 色2)
    塗りつぶ_開始()
    畫圓(半径の長さ*0.15)
    塗りつぶ_終わり()
    左(90)
    アップ_ペン()
    後退(半径の長さ*0.35)
    ダウン_ペン()
    左(90)

def 主な機能():
    リセット()
    陰陽(200, 黒, 白)
    陰陽(200, 白, 黒)
    隠すカメ()
    return "終わり!"

if __name__ == '__main__':
    メッセージ=主な機能()
    印刷(メッセージ)
    メインループ()
