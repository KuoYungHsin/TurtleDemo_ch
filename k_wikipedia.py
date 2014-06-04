# -*- coding: utf-8 -*-
"""      turtle-example-suite:

          tdemo_wikipedia3.py

This example is
inspired by the Wikipedia article on turtle
graphics. (See example wikipedia1 for URLs)

First we create (ne-1) (i.e. 35 in this
example) copies of our first turtle p.
Then we let them perform their steps in
parallel.

Followed by a complete 回復().
"""
from turtle_tc_01 import *
from time import clock, sleep

def mn_eck(p, ne,sz):
    turtlelist = [p]
    #create ne-1 additional 龜群
    for i in 範圍(1,ne):
        q = p.複製()
        q.右轉(360.0/ne)
        turtlelist.append(q)
        p = q
    for i in 範圍(ne):
        c = abs(ne/2.0-i)/(ne*.7)
        # let those ne 龜群 make a step
        # in parallel:
        for t in turtlelist:
            t.右轉(360./ne)
            t.筆色(1-c,0,c)
            t.後退(sz)

def 主函數():
    s = 幕類()
    s.背景色(黑)
    p=龜類()
    p.速度(0)
    p.藏龜()
    p.筆色(紅)
    p.筆粗(3)

    s.追蹤(36,0)

    at = clock()
    mn_eck(p, 36, 19)
    et = clock()
    z1 = et-at

    sleep(1)

    at = clock()
    while any([t.回復暫存區的個數() for t in s.龜群()]):
        for t in s.龜群():
            t.回復()
    et = clock()
    return "runtime: %.3f sec" % (z1+et-at)


if __name__ == '__main__':
    訊息  = 主函數()
    印(訊息)
    主迴圈()
