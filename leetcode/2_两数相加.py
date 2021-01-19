#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
2. 两数相加
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。



示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]


提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
"""

from datastructure import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        d, m = divmod(l1.val + l2.val, 10)
        head.val = m
        while all([l1.next, l2.next]):
            l1 = l1.next
            l2 = l2.next
            l1.val += d
            d, m = divmod(l1.val + l2.val, 10)
            l1.val = m
        l1.next = l1.next if l1.next else l2.next
        while l1.next and d:
            l1 = l1.next
            d, m = divmod(l1.val + d, 10)
            l1.val = m
        if d:
            l1.next = ListNode(val=d)
        return head

    def fastest(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp = 0
        res = ans = ListNode(None)
        while l1 or l2 or tmp:
            tmp += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            res.next = ListNode(tmp % 10)
            tmp //= 10
            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ans.next
