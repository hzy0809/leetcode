#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/8 17:37
# @File    : 102_二叉树的层序遍历.py
# @Software: PyCharm

"""
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。



示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
示例 2：

输入：root = [1]
输出：[[1]]
示例 3：

输入：root = []
输出：[]


提示：

树中节点数目在范围 [0, 2000] 内
-1000 <= Node.val <= 1000


链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
"""
from collections import deque
from typing import List

from leetcode.datastructure import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        temp = [root]
        while temp:
            stack = []
            result.append([t.val for t in temp])
            for node in temp:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            temp = stack
        return result


class FSolution(Solution):
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res
