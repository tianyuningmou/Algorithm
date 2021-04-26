# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 207-课程表.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/26 3:06 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/26 3:06 下午
"""

"""
207. 课程表
你这个学期必须选修 numCourses 门课程，记为0到numCourses - 1 。在选修某些课程之前需要一些先修课程。 
先修课程按数组prerequisites 给出，其中prerequisites[i] = [ai, bi]，表示如果要学习课程ai则必须先学习课程bi 。
例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
"""

import collections


class Solution(object):
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        result = list()
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            result.append(u)

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        return valid
