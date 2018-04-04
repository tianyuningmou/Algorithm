# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: ugly_number.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/4/4 下午8:02

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/4/4 下午8:02
"""


# 求出第N个丑数
class Solution:
    def get_ugly_number(self, index):
        n, m = 0, 0
        k1, k2, k3 = [1], [1], [1]
        while n < index:
            m = min(k1[0], k2[0], k3[0])
            n += 1
            if m in k1:
                k1.remove(m)
            if m in k2:
                k2.remove(m)
            if m in k3:
                k3.remove(m)
            k1.append(m*2)
            k2.append(m*3)
            k3.append(m*5)
        return m


if __name__ == '__main__':
    solution = Solution()
    result = solution.get_ugly_number(14)
    print(result)
