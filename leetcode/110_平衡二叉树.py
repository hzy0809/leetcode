#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/8 17:47
# @File    : 110_平衡二叉树.py
# @Software: PyCharm
"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1 。



示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：true
示例 2：


输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
示例 3：

输入：root = []
输出：true


提示：

树中的节点数在范围 [0, 5000] 内
-104 <= Node.val <= 104

链接：https://leetcode-cn.com/problems/balanced-binary-tree
"""
from leetcode.datastructure import TreeNode, convert_list2tree


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def deepth(node):
            if not node:
                return 0, True
            left, l = deepth(node.left)
            right, r = deepth(node.right)

            if l and r and abs(left - right) <= 1:
                return max(left, right) + 1, True
            return 0, False

        _, res = deepth(root)
        return res


class BSolution(Solution):
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node):
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            else:
                return max(left_height, right_height) + 1

        return height(root) >= 0


if __name__ == '__main__':
    import json

    _data = '[3,9,20,null,null,15,7]'
    data = json.loads(_data)
    head = convert_list2tree(data)
    print(Solution().isBalanced(head))
