# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 95-不同的搜索二叉树II.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/3/30 6:49 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/3/30 6:49 下午
"""

"""
95. 不同的搜索二叉树II
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树
"""


from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    @classmethod
    def generateTrees(cls, n: int) -> List[TreeNode]:
        def generate(start, end):
            if start > end:
                return [None, ]
            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate(start, i - 1)
                right_trees = generate(i + 1, end)
                for l in left_trees:
                    for r in right_trees:
                        curNode = TreeNode(i)
                        curNode.left = l
                        curNode.right = r
                        all_trees.append(curNode)

            return all_trees

        return generate(1, n) if n else []


if __name__ == '__main__':
    print(Solution.generateTrees(4))
