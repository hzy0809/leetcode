#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/11 15:16
# @File    : 21_合并两个有序链表.py
# @Software: PyCharm

"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。


示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]

提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列

链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from typing import Optional

from leetcode.datastructure import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def recur_func(a, b):
            if not a or not b:
                return a or b
            if a.val < b.val:
                next_node = recur_func(a.next, b)
                a.next = next_node
                return a
            else:
                next_node = recur_func(a, b.next)
                b.next = next_node
                return b

        return recur_func(list1, list2)


class FastSolution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(None)
        node = res
        while l1 and l2:
            if l1.val < l2.val:
                node.next, l1 = l1, l1.next
            else:
                node.next, l2 = l2, l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return res.next
