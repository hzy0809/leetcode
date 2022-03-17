#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/17 18:41
# @File    : 226_翻转二叉树.py
# @Software: PyCharm
"""
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。



示例 1：



输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
示例 2：



输入：root = [2,1,3]
输出：[2,3,1]
示例 3：

输入：root = []
输出：[]


提示：

树中节点数目范围在 [0, 100] 内
-100 <= Node.val <= 100

链接：https://leetcode-cn.com/problems/invert-binary-tree
"""
from leetcode.datastructure import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        node_list = [root]
        while node_list:
            res = []
            for node in node_list:
                node.left, node.right = node.right, node.left
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
            node_list = res
        return root


class RSolution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
