# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 236.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/13 3:26 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/13 3:26 下午
"""


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):

    @classmethod
    def lowestCommonAncestor(cls, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(root, p, q):
            if not root:
                return None
            lson = dfs(root.left, p, q)
            rson = dfs(root.right, p, q)
            if (lson and rson) or ((root.val == p.val or root.val == q.val) and (lson or rson)):
                return root
            return lson or rson or (root.val == p.val or root.val == q.val)

        root = dfs(root, p, q)
        return root


if __name__ == '__main__':
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_1 = TreeNode(1, node_2, node_3)
    Solution.lowestCommonAncestor(node_1, node_2, node_3)
