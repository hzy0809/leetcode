#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个链表，旋转链表，将链表每个节点向右移动k个位置，其中k是非负数。

示例1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步:0->1->2->NULL
向右旋转 4 步:2->0->1->NULL


链接：https://leetcode-cn.com/problems/rotate-list

"""

from datastructure import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        需要获取头指针，尾指针，旋转后的头指针，尾指针
        可以不使用列表，第一次遍历获取长度和尾指针，第二次遍历获取旋转后的头尾指针
        :param head:头指针
        :param k:右移长度
        :return:
        """
        if not head:
            return head
        temp = list()
        while head:
            temp.append(head)
            head = head.next
        k = k % len(temp)
        if k:
            temp[-k - 1].next = None
            temp[-1].next = temp[0]
            temp = temp[-k:] + temp[:-k]
        return temp[0]
