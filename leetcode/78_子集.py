#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 13:06
# @Author  : hzy
# @File    : 78_子集.py
# @Software: PyCharm
"""
给你一个整数数组nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。



示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]


提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同

链接：https://leetcode-cn.com/problems/subsets
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)
        for i in range(n):
            m = len(res)
            j = 0
            num = nums[i]
            while j < m:
                new = res[j].copy()
                new.append(num)
                res.append(new)
                j += 1
        return res

    def search_node(self, nums: List[int]) -> List[List[int]]:
        """
        递归搜索，保留节点信息
        :param nums:
        :return:
        """
        res = []
        n = len(nums)
        self._search(0, n, nums, [], res)
        return res

    def _search(self, start, n, num, path, res):
        res.append(path[:])
        for i in range(start, n):
            path.append(num[i])
            self._search(i + 1, n, num, path, res)
            path.pop()

    def bitrun(self, nums: List[int]) -> List[List[int]]:
        """
        位运算
        :param nums:
        :return:
        """
        size = len(nums)
        n = 1 << size  # 组合数
        res = []
        for i in range(n):
            cur = []
            for j in range(size):
                # 判断位数上是否为1
                if i >> j & 1:
                    cur.append(nums[j])
            res.append(cur)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.bitrun([1, 2, 3]))
