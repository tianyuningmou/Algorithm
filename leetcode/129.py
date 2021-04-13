# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 129.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/13 10:37 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/13 10:37 上午
"""

"""
129. 求根节点到叶节点数字之和
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：
例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的所有数字之和 。
叶节点是指没有子节点的节点。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumNumbers(self, root: TreeNode) -> int:

        def calc_num(root, ans):
            if not root:
                return 0
            ans.append(str(root.val))
            if not root.left and not root.right:
                res.append(ans[:])
            if root.left:
                calc_num(root.left, ans)
                ans.pop()
            if root.right:
                calc_num(root.right, ans)
                ans.pop()

        res = []
        calc_num(root, [])
        res_num = 0
        for i in res:
            num = int(''.join(i))
            res_num += num
        return res_num
