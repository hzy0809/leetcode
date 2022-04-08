#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/8 16:03
# @File    : 94_二叉树的中序遍历.py
# @Software: PyCharm
"""
给定一个二叉树的根节点 root ，返回 它的 中序遍历 。



示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]


提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100


进阶:递归算法很简单，你可以通过迭代算法完成吗？

链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
"""
from typing import Optional, List

from leetcode.datastructure import TreeNode, convert_list2tree


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        def dfs(node):
            if node.left:
                dfs(node.left)
            result.append(node.val)
            if node.right:
                dfs(node.right)

        dfs(root)
        return result


class IterSolution(Solution):
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        temp = [root]
        check = set()
        c = True
        while c:
            t = []
            c = False
            while temp:
                node = temp.pop()
                if node in check:
                    t.append(node)
                    continue
                check.add(node)
                if node.right:
                    c = True
                    t.append(node.right)
                t.append(node)
                if node.left:
                    c = True
                    t.append(node.left)
            temp = t[::-1]
        return [t.val for t in temp]


class BSolution(Solution):
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


if __name__ == '__main__':
    import json

    _data = json.loads('[2,3,4,null,1]')
    data = convert_list2tree(_data)
    print(BSolution().inorderTraversal(data))
