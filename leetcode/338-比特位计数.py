# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 338-比特位计数.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/22 2:40 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/22 2:40 下午
"""

"""
338. 比特位计数
给定一个非负整数num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:
    输入: 2
    输出: [0,1,1]

示例2:
    输入: 5
    输出: [0,1,1,2,1,2]
"""


class Solution(object):
    def countBits(self, num: int):
        bits = [0]
        highBit = 0
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                highBit = i
            bits.append(bits[i - highBit] + 1)
        return bits


if __name__ == '__main__':
    Solution().countBits(5)
