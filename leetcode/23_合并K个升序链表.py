#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: 23_合并K个升序链表.py
# @time: 2022/3/21 22:00
"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。



示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]


提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4

链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
"""
from typing import Optional, List

from leetcode.datastructure import ListNode
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode()
        if not lists:
            return result.next
        mapping = {node: node.val for node in lists if node}
        if not mapping:
            return result.next
        head = result
        while mapping:
            node = min(mapping, key=lambda n: n.val)
            head.next = node
            mapping.pop(node)
            if node.next:
                mapping[node.next] = node.next.val
        return result.next


class PartitionSolution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        amount = len(lists)
        while amount > 1:
            for i in range(amount // 2):
                lists.append(self.merge2node(lists.pop(), lists.pop()))
            amount = len(lists)
        return lists[0] if amount else None

    def merge2node(self, left, right):
        head = ListNode()
        res = head
        while left and right:
            if left.val > right.val:
                head.next = right
                right = right.next
            else:
                head.next = left
                left = left.next
            head = head.next
        head.next = left if left else right
        return res.next


class QueueSolution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        index = 0
        result = []
        for node in lists:
            while node:
                heapq.heappush(result, (node.val, index, node))
                node = node.next
                index += 1
        head = ListNode()
        op = head
        while result:
            _, _, head.next = heapq.heappop(result)
            head = head.next
        return op.next


class FQueueSolution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        index = 0
        result = []
        head = ListNode()
        op = head
        for node in lists:
            heapq.heappush(result, (node.val, index, node))
            index += 1

        while result:
            _, _, node = heapq.heappop(result)
            head.next = node
            head = head.next
            if node.next:
                heapq.heappush(result, (node.next.val, index, node.next))
                index += 1
        return op.next
