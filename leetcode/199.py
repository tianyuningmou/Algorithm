# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 199.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/12 6:27 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/12 6:27 下午
"""

"""
199. 二叉树的右视图
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。 
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rightSideView(self, root: TreeNode):
        ans = list()
        if not root:
            return ans
        right_list = [root]
        while right_list:
            length = len(right_list)
            for i in range(length):
                node = right_list.pop(0)
                if node.left:
                    right_list.append(node.left)
                if node.right:
                    right_list.append(node.right)
                if i == length - 1:
                    ans.append(node.val)
        return ans
