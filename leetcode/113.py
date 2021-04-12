# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 113.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/12 6:12 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/12 6:12 下午
"""

"""
113. 路径总和II
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root: TreeNode, targetSum: int):
        def search(root, targetSum, ans):
            if not root:
                return []
            ans.append(root.val)
            if not root.left and not root.right and targetSum == root.val:
                res.append(ans[:])
            if root.left:
                search(root.left, targetSum - root.val, ans)
                ans.pop()
            if root.right:
                search(root.right, targetSum - root.val, ans)
                ans.pop()

        res = []
        search(root, targetSum, [])
        return res
