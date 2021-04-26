# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 142-环形链表II.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/26 11:01 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/26 11:01 上午
"""

"""
142. 环形链表II
给定一个链表，返回链表开始入环的第一个节点。如果链表无环，则返回null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
说明：不允许修改给定的链表。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        slow = fast = head
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return None
            if fast == slow:
                ptr = head
                while ptr != slow:
                    slow = slow.next
                    ptr = ptr.next
                return ptr
        return None
