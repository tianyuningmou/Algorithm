# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 236-二叉树的最近公共祖先.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/13 3:26 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/13 3:26 下午
"""

"""
236. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
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
