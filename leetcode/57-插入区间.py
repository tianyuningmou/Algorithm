# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 57-插入区间.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/5/24 4:20 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/5/24 4:20 下午
"""

"""
57. 插入区间
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        left, right = newInterval
        placed = False
        ans = []
        for li, ri in intervals:
            if li > right:
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                ans.append([li, ri])
            else:
                left = min(left, li)
                right = max(right, ri)
        if not placed:
            ans.append([left, right])
        return ans
