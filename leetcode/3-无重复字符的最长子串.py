# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 3-无重复字符的最长子串.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/15 3:54 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/15 3:54 下午
"""

"""
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
"""


def lengthOfLongestSubstring(s):
    length = len(s)
    ans, right, occ = 0, -1, set()
    for left in range(length):
        if left != 0:
            occ.remove(s[left - 1])
        while right + 1 < length and s[right + 1] not in occ:
            occ.add(s[right + 1])
            right += 1
        ans = max(ans, right - left + 1)
    return ans


if __name__ == '__main__':
    print(lengthOfLongestSubstring('abcabcbb'))
