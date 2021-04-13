# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 222.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/13 10:19 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/13 10:19 上午
"""

"""
222. 完全二叉树的节点个数
给你一棵完全二叉树的根节点 root，求出该树的节点个数。
完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~2的h次方个节点。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return len(res)
