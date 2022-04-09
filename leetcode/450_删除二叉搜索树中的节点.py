#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: 450_删除二叉搜索树中的节点.py
# @time: 2022/4/9 11:39
"""

"""
from typing import Optional

from leetcode.datastructure import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        prev = None
        head = root
        while root:
            if root.val > key:
                prev = root
                root = root.left
            elif root.val < key:
                prev = root
                root = root.right
            else:
                node = root.right
                if not node:
                    root.right = root.left
                else:
                    while node.left:
                        node = node.left
                    node.left = root.left
                if not prev:
                    return root.right
                elif prev.val > key:
                    prev.left = root.right
                else:
                    prev.right = root.right
                break
        return head


class BSolution(Solution):
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == key:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            tmp = root.right.left
            root.right.left = root.left
            it = root.left
            while it.right is not None:
                it = it.right
            it.right = tmp
            return root.right
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root
