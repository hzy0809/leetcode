#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/17 17:27
# @File    : 101_对称二叉树.py
# @Software: PyCharm

"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。



示例 1：


输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：


输入：root = [1,2,2,null,3,null,3]
输出：false


提示：

树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100

链接：https://leetcode-cn.com/problems/symmetric-tree
"""
from leetcode.datastructure import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        node_list = [root.left, root.right]
        while node_list:
            value_list = [node.val if node else None for node in node_list]
            if not value_list == value_list[::-1]:
                return False
            _next_list = []
            fuc = _next_list.append
            for node in node_list:
                if node:
                    fuc(node.left)
                    fuc(node.right)
            node_list = _next_list
        return True


class FastSolution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def is_sym(left, right):
            if not left and not right:
                return True
            if not all({left, right}):
                return False
            if left.val != right.val:
                return False
            return is_sym(left.left, right.right) and is_sym(left.right, right.left)

        return is_sym(root.left, root.right)
