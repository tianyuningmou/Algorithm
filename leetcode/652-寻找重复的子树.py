# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 652-寻找重复的子树.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/19 3:59 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/19 3:59 下午
"""

"""
652. 寻找重复的子树
给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
两棵树重复是指它们具有相同的结构以及相同的结点值。
"""

import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findDuplicateSubtrees(self, root: TreeNode):
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        res = []
        count = collections.Counter()

        def dfs(root):
            if root:
                tree = trees[root.val, dfs(root.left), dfs(root.right)]
                count[tree] += 1
                if count[tree] == 2:
                    res.append(root)
                return tree

        dfs(root)
        return res


if __name__ == '__main__':
    nums_2 = TreeNode(2)
    nums_2_1 = TreeNode(2)
    nums_1 = TreeNode(1, nums_2, nums_2_1)
    print(Solution().findDuplicateSubtrees(nums_1))
