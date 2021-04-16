# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 508-出现次数最多的子树元素和.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/16 6:41 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/16 6:41 下午
"""

"""
508. 出现次数最多的子树元素和
给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root: TreeNode):

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            total = root.val + left + right
            res_dict[total] = res_dict.get(total, 0) + 1
            return total

        res_dict = dict()
        dfs(root)
        # 对各子树元素和，按出现次数从大到小排序
        sorted_hash = sorted(res_dict.items(), key=lambda x: x[1], reverse=True)
        # 取前面所有次数最多且相同的子树元素和
        res = [sorted_hash[i][0] for i in range(len(sorted_hash)) if sorted_hash[i][1] == sorted_hash[0][1]]
        return res
