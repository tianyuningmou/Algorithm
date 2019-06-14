# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: place_order.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/5/28 上午10:02

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/5/28 上午10:02
"""

import sys

results = sys.stdin.readline().strip().split()
good_num = results[0]
pref_num = results[1]
discount_price = 0
discount_price_final = 0
for i in range(int(good_num)):
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    discount_price += values[0]
    if values[1] == 1:
        discount_price_final += values[0] * 0.8
    else:
        discount_price_final += values[0]
final_list = []
final_price = 0
for j in range(int(pref_num)):
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    if discount_price >= values[0]:
        final_price = discount_price - values[1]
        final_list.append(final_price)
final_price = min(final_list)
final_price = final_price if final_price < discount_price_final else discount_price_final
print("%.2f" % final_price)
