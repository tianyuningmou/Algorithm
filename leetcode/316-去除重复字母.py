# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 316-去除重复字母.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/6/28 11:23 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/6/28 11:23 上午
"""

"""
316. 去除重复字母
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）
"""


class Solution(object):

    def removeDuplicateLetters(self, s):
        visited = [False for _ in range(26)]
        nums = [0 for _ in range(26)]
        for st in s:
            nums[ord(st) - ord('a')] += 1
        res = []
        for st in s:
            if not visited[ord(st) - ord('a')]:
                while len(res) > 0 and res[-1] > st:
                    if nums[ord(res[-1]) - ord('a')] > 0:
                        visited[ord(res[-1]) - ord('a')] = False
                        res.pop()
                    else:
                        break
                visited[ord(st) - ord('a')] = True
                res.append(st)
            nums[ord(st) - ord('a')] -= 1
        return ''.join(res)


if __name__ == '__main__':
    print(Solution().removeDuplicateLetters('cbacdcbc'))
