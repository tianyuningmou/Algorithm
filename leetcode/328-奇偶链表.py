# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 328-奇偶链表.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/6/16 5:49 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/6/16 5:49 下午
"""

"""
328. 奇偶链表
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        evenHead = head.next
        odd, even = head, evenHead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
