# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 567-字符串的排列.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/7/25 2:32 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/7/25 2:32 下午
"""

"""
567. 字符串的排列
判断s2中是否包含s1所有字母的任意排列
"""

class Solution(object):

    def checkInclusion(self, s1, s2):
        length_1 = len(s1)
        length_2 = len(s2)
        if length_1 > length_2:
            return False
        cnt_1 = [0] * 26
        cnt_2 = [0] * 26
        for i in range(length_1):
            cnt_1[ord(s1[i]) - ord('a')] += 1
            cnt_2[ord(s2[i]) - ord('a')] += 1
        if cnt_1 == cnt_2:
            return True
        for i in range(length_1, length_2):
            cnt_2[ord(s2[i]) - ord('a')] += 1
            cnt_2[ord(s2[i - length_1]) - ord('a')] -= 1
            if cnt_1 == cnt_2:
                return True
        return False


if __name__ == '__main__':
    print(Solution().checkInclusion("ab", "eidbaooo"))
