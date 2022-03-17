#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/17 18:17
# @File    : 104_二叉树的最大深度.py
# @Software: PyCharm
"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明:叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度3 。


链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
"""
from typing import Optional

from leetcode.datastructure import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        deep = 0
        node_list = [root]
        while node_list:
            deep += 1
            res = []
            for node in node_list:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
            node_list = res
        return deep


class RSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def deep(node):
            if not node:
                return 0
            if node.left and not node.right:
                return 1
            return 1 + max({deep(node.left), deep(node.right)})

        return deep(root)
