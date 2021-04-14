# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 111-二叉树的最小深度.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/12 4:30 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/12 4:30 下午
"""

"""
111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
"""

from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # 深度优先搜索
    def minDepth(self, root: TreeNode) -> int:

        def get_min_depth(root, ans):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            if root.left:
                left_depth = get_min_depth(root.left, ans)
                ans = min(ans, left_depth + 1)
            if root.right:
                right_depth = get_min_depth(root.right, ans)
                ans = min(ans, right_depth + 1)
            return ans

        ans = 100000
        ans = get_min_depth(root, ans)
        return ans

    # 广度优先搜索
    def min_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return 0
