# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 6-Z字形变换.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/5/8 3:19 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/5/8 3:19 下午
"""

"""
6. Z字形变换
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
"""


class Solution(object):
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if numRows == 1 or numRows >= length: return s
        res = [[] for _ in range(numRows)]
        curRow = 0
        flag = 1
        for s_ in s:
            if curRow == 0:
                res[curRow].append(s_)
                flag = 1
                curRow += flag
            elif curRow == numRows - 1:
                res[curRow].append(s_)
                flag = -1
                curRow += flag
            else:
                res[curRow].append(s_)
                curRow += flag
        ans = ''
        for r in res:
            ans += ''.join(r)
        return ans


if __name__ == '__main__':
    print(Solution().convert("PAYPALISHIRING", 3))
