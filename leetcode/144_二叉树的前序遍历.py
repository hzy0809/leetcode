#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: 144_二叉树的前序遍历.py
# @time: 2022/4/9 9:44

"""
给你二叉树的根节点 root ，返回它节点值的前序遍历。



示例 1：


输入：root = [1,null,2,3]
输出：[1,2,3]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[1,2]
示例 5：


输入：root = [1,null,2]
输出：[1,2]


提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100


进阶：递归算法很简单，你可以通过迭代算法完成吗？

链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
"""
from collections import deque
from typing import Optional, List

from leetcode.datastructure import TreeNode, convert_list2tree


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        def dfs(node):
            res.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        return res


class IterSolution(Solution):
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res


if __name__ == '__main__':
    import json

    d = "[2,1,3,null,4]"
    data = convert_list2tree(json.loads(d))
    print(IterSolution().preorderTraversal(data))
