# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 394-字符串编码.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/27 2:27 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/27 2:27 下午
"""

"""
394. 字符串编码
"""


class Solution(object):
    def decodeString(self, s: str) -> str:
        stack = list()
        length = len(s)
        i = length - 1
        while i >= 0:
            if s[i].isdigit() is False:
                stack.append(s[i])
                i -= 1
            else:
                num = ''
                while i >= 0 and s[i].isdigit():
                    num = s[i] + num
                    i -= 1
                sub = ''
                while stack[-1] != ']':
                    tmp = stack.pop()
                    if tmp != '[':
                        sub += tmp
                stack.pop()
                sub = int(num) * sub
                stack.append(sub)

        stack.reverse()
        return ''.join(stack)


if __name__ == '__main__':
    print(Solution().decodeString("3[a]2[bc]"))
