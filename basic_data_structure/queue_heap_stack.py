# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: queue_heap_stack.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/5/15 下午5:03

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/5/15 下午5:03
"""

"""
Queue是一个FIFO（先进先出）的数据结构，并发中使用较多，可以安全地将对象从一个任务传给另一个任务。
    Queue和Stack在Python中都是有list，[]实现的。在python中list是一个dynamic array，可以通过append在list的尾部添加元素， 
        通过pop()在list的尾部弹出元素实现Stack的FILO，如果是pop(0)则弹出头部的元素实现Queue的FIFO。
    Python中提供heapq的lib来实现priority queue，提供push和pop两个基本操作和heapify初始化操作。
    Python的list就可以执行类似deque的操作，但是效率会过于慢。
        为了提升处理效率，高效的数据结构放在了collections中。在collections中提供了deque类。

堆通常指的是二叉堆，二叉堆是一个近似完全二叉树的数据结构，即披着二叉树羊皮的数组，故使用数组来实现较为便利。
    子结点的键值或索引总是小于（或者大于）它的父节点，且每个节点的左右子树又是一个二叉堆(大根堆或者小根堆)。
    根节点最大的堆叫做最大堆或大根堆，根节点最小的堆叫做最小堆或小根堆。常被用作实现优先队列

list作为最基本的python数据结构之一，可以很轻松的实现stack。如果需要更高效的stack，建议使用deque。
"""


# class MaxHeap:
#
#     def __init__(self, array=None):
#         if array:
#             self.heap = self.max_heapify(array)
#         else:
#             self.heap = []
#
#     def sink(self, array, i):
#         left, right = 2 * i + 1, 2 * i + 2
#         max_index = i
#         flag = array[left] > array[right]
#         if left < len(array) and array[left] > array[max_index] and flag:
#             max_index = left
#         if right < len(array) and array[right] > array[max_index] and flag:
#             max_index = right
#         if max_index != i:
#             array[i], array[max_index] = array[max_index], array[i]
#             self.sink(array, max_index)
#
#     def swim(self, array, i):
#         if i == 0:
#             return
#         father = int((i - 1) / 2)
#         if array[father] < array[i]:
#             array[father], array[i] = array[i], array[father]
#             self.swim(array, father)
#
#     def max_heapify(self, array):
#         for i in range(int(len(array) / 2) - 1, -1, -1):
#             self.sink(array, i)
#         return array
#
#     def push(self, item):
#         self.heap.append(item)
#         self.swim(self.heap, len(self.heap) - 1)
#
#     def pop(self):
#         self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
#         item = self.heap.pop()
#         self.sink(self.heap, 0)
#         return item
