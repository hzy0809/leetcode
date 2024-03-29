#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/17 19:12
# @File    : 236_二叉树的最近公共祖先.py
# @Software: PyCharm

"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”



示例 1：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
示例 2：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
示例 3：

输入：root = [1,2], p = 1, q = 2
输出：1


提示：

树中节点数目在范围 [2, 105] 内。
-109 <= Node.val <= 109
所有 Node.val 互不相同 。
p != q
p 和 q 均存在于给定的二叉树中。


链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
"""
from leetcode.datastructure import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pq = {p.val, q.val}
        if root.val in pq:
            return root

        def lowest(node):
            if not node:
                return None
            res = lowest(node.left)

            if not pq:
                return res

            if node.val in pq:
                pq.remove(node.val)
                res = node

            if not pq:
                return res

            right = lowest(node.right)

            if res and right:
                res = node
            return res or right

        return lowest(root)


class FastSolution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


class MinSolution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        ddict = dict()
        nodes = {p, q}
        import collections
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node in nodes:
                nodes.remove(node)
            if not nodes:
                break
            if node.left:
                ddict[node.left] = node
                queue.append(node.left)
            if node.right:
                ddict[node.right] = node
                queue.append(node.right)
        l1 = p
        l2 = q
        # 两个链表相交
        # a + nb    b + na
        while l1 != l2:
            l1 = ddict.get(l1, q)
            l2 = ddict.get(l2, p)
        return l1

        # 两个链表相交
        # l2_set = set()
        # while l2:
        #     l2_set.add(l2)
        #     l2 = ddict.get(l2, None)
        # while l1:
        #     if l1 in l2_set:
        #         return l1
        #     l1 = ddict.get(l1, None)
