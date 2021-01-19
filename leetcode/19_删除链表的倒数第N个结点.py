#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给你一个链表，删除链表的倒数第n个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？


示例 1：


输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]


提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz



链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
"""
from datastructure import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        a = head
        temp = []
        while a:
            temp.append(a)
            a = a.next
        if 1 < n < len(temp):
            temp[-(n + 1)].next = temp[-(n - 1)]
        elif n == 1 and len(temp) > 1:
            temp[-(n + 1)].next = None
        elif n == len(temp):
            head = head.next
        return head

    def best(self, head: ListNode, n: int) -> ListNode:
        """
        双指针，前指针超前后指针n+1,删除后指针的next
        :param head:
        :param n:
        :return:
        """
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next
