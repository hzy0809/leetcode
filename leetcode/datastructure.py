#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ListNode(object):
    """
    linkNode
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node(object):

    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


if __name__ == '__main__':
    a = ListNode(0)
    b = ListNode(a, 1)
    print(b.val)
