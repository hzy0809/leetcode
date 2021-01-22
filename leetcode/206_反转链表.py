#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

链接：https://leetcode-cn.com/problems/reverse-linked-list
"""

from datastructure import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # """迭代"""
        # n = temp = None
        # while head:
        #     n,head = head,head.next
        #     n.next = temp
        #     temp = n
        # return n

        """递归"""
        if head is None or head.next is None:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead
