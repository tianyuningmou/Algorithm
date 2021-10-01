# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 437-路径总和III.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/10/1 10:43 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/10/1 10:43 上午
"""

"""
437. 路径总和III
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root: TreeNode, targetSum: int):
        def rootSum(root: TreeNode, targetSum: int):
            if root is None:
                return 0
            ret = 0
            if root.val == targetSum:
                ret += 1
            ret += rootSum(root.left, targetSum - root.val)
            ret += rootSum(root.right, targetSum - root.val)
            return ret

        if root is None:
            return 0
        ret = rootSum(root, targetSum)
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)
        return ret

