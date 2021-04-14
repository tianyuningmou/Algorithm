# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 117-填充每个节点的下一个右侧节点指针II.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/12 5:32 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/12 5:32 下午
"""

"""
117. 填充每个节点的下一个右侧节点指针II
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    @classmethod
    def connect(cls, root: 'Node') -> 'Node':
        if not root:
            return None
        from collections import deque
        queue = deque([root])
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i < length - 1:
                    node.next = queue[0]

        return root


if __name__ == '__main__':
    node_7 = Node(7)
    node_5 = Node(5)
    node_4 = Node(4)
    node_3 = Node(3, right=node_7)
    node_2 = Node(2, node_4, node_5)
    node_1 = Node(1, node_2, node_3)
    Solution.connect(node_1)
