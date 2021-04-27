# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 406-根据身高重建队列.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/27 3:47 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/27 3:47 下午
"""

"""
406. 根据身高重建队列
"""


class Solution(object):
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        ans = [[] for _ in range(n)]
        for person in people:
            spaces = person[1] + 1
            for i in range(n):
                if not ans[i]:
                    spaces -= 1
                    if spaces == 0:
                        ans[i] = person
                        break
        return ans


if __name__ == '__main__':
    Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
