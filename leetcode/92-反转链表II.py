# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 92-反转链表II.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/6/16 10:40 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/6/16 10:40 上午
"""

"""
92. 反转链表II
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy_node = ListNode(0, head)
        prev = dummy_node
        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next
        for _ in range(right - left):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        return dummy_node.next


if __name__ == '__main__':
    node_5 = ListNode(5)
    node_4 = ListNode(4, node_5)
    node_3 = ListNode(3, node_4)
    node_2 = ListNode(2, node_3)
    node_1 = ListNode(1, node_2)
    Solution().reverseBetween(node_1, 2, 4)
