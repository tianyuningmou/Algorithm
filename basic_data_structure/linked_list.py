# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: linked_list.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/5/14 上午10:58

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/5/14 上午10:58
"""

"""
链表是线性表的一种
    线性表中数据元素之间的关系是一对一的关系，即除了第一个和最后一个数据元素之外，其它数据元素都是首尾相接的。
    线性表有两种存储方式，一种是顺序存储结构，另一种是链式存储结构。
    
链表指针的鲁棒性：
    ① 当访问链表中某个节点 curt.next 时，一定要先判断 curt 是否为 None
    ② 全部操作结束后，判断是否有环；若有环，则置其中一端为 None
"""


# 反转单向链表
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev


# 反转双向链表
class DListNode:

    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

    def reverse(self, head):
        curt = None
        while head:
            curt = head
            head = curt.next
            curt.next = curt.prev
            curt.prev = head
        return curt


# 快慢指针
class NodeCircle:

    def __init__(self, val):
        self.val = val
        self.next = None


    def has_circle(self, head):
        slow = head
        fast = head
        while (slow and fast):
            fast = fast.next
            slow = slow.next
            if fast:
                fast = fast.next
            if fast == slow:
                break
        if fast and slow and (fast == slow):
            return True
        else:
            return False
