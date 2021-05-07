# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 124-二叉树中的最大路径和.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/5/7 3:20 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/5/7 3:20 下午
"""

"""
124. 二叉树中的最大路径和
路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中至多出现一次。
该路径至少包含一个节点，且不一定经过根节点。
路径和是路径中各节点值的总和。
给你一个二叉树的根节点root，返回其最大路径和 。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)
            newPath = node.val + leftGain + rightGain
            self.maxSum = max(self.maxSum, newPath)
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum
