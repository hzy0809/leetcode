#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: 145_二叉树的后序遍历.py
# @time: 2022/4/9 10:15

"""
给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。



示例 1：


输入：root = [1,null,2,3]
输出：[3,2,1]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]


提示：

树中节点的数目在范围 [0, 100] 内
-100 <= Node.val <= 100


进阶：递归算法很简单，你可以通过迭代算法完成吗？

链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
"""
from typing import Optional, List

from leetcode.datastructure import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []

        def dfs(node):
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res


class IterSolution(Solution):
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res
