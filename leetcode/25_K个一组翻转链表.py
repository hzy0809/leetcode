#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给你一个链表，每k个节点一组进行翻转，请你返回翻转后的链表。

k是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。



示例：

给你这个链表：1->2->3->4->5

当k= 2 时，应当返回: 2->1->4->3->5

当k= 3 时，应当返回: 3->2->1->4->5



说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。



链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group

"""

from datastructure import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        result = t = ListNode(0, head)
        temp = head
        k_list = list()
        while temp:
            k_list.append(temp)
            temp = temp.next
            if len(k_list) == k:
                h_node = k_list[-1].next
                for i in range(1, k):
                    k_list[i].next = k_list[i - 1]
                k_list[0].next = h_node
                t.next = k_list[-1]
                t = k_list[0]
                k_list = list()
        return result.next
