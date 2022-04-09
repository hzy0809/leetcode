#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: 98_验证二叉搜索树.py
# @time: 2022/4/9 10:39
"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。


示例 1：


输入：root = [2,1,3]
输出：true
示例 2：


输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。


提示：

树中节点数目范围在[1, 104] 内
-231 <= Node.val <= 231 - 1

链接：https://leetcode-cn.com/problems/validate-binary-search-tree
"""
from leetcode.datastructure import TreeNode, convert_list2tree


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        temp = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            temp.append(node.val)
            dfs(node.right)

        dfs(root)
        if len(temp) <= 1:
            return True

        for i in range(len(temp) - 1):
            if temp[i + 1] <= temp[i]:
                return False
        return True


class BSolution(Solution):
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, min=None, max=None):
            if not node:
                return True
            left = dfs(node.left, min=min, max=node.val)
            if min is not None and node.val <= min:
                return False
            if max is not None and node.val >= max:
                return False
            right = dfs(node.right, min=node.val, max=max)
            return left and right

        return dfs(root)


class IterSolution(Solution):
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        temp = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if temp is None:
                temp = root.val
            else:
                if root.val <= temp:
                    return False
                temp = root.val
            root = root.right
        return True


if __name__ == '__main__':
    data = [5, 1, 4, None, None, 3, 6]
    print(IterSolution().isValidBST(convert_list2tree(data)))
