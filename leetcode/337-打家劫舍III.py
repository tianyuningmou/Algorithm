# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 337-打家劫舍III.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/13 3:56 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/13 3:56 下午
"""

"""
337. 打家劫舍III
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。
这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rob(self, root: TreeNode) -> int:

        def dfs(root):
            if not root:
                return [0, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            selected = root.val + left[1] + right[1]
            notSelected = max(left[0], left[1]) + max(right[0], right[1])
            return [selected, notSelected]

        rootStatus = dfs(root)
        return max(rootStatus[0], rootStatus[1])

