#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List


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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.val)


def convert_list2tree(tl: List[int]):
    if not tl:
        return None
    nl = [TreeNode(val=t) for t in tl]
    head = nl[0]
    temp = [nl.pop(0)]
    while nl:
        root = temp.pop(0)
        left = nl.pop(0)
        if left.val is not None:
            root.left = left
            temp.append(left)
        if nl:
            right = nl.pop(0)
            if right.val is not None:
                root.right = right
                temp.append(right)
    return head


if __name__ == '__main__':
    # a = ListNode(0)
    # b = ListNode(a, 1)
    # print(b.val)
    head = convert_list2tree([1, None, 2, 3])
    print(head)
    import heapq
    heapq.heappushpop()
