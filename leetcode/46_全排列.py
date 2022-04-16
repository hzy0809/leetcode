#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: 46_全排列.py
# @time: 2022/4/6 21:26
"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。



示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]


提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同

链接：https://leetcode-cn.com/problems/permutations
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)

        def dfs(n: List[int], t, l):
            if not l:
                res.append(t[:])
            for i in range(l):
                t.append(i)
                dfs(n[0: i] + n[i + 1:l], t, l - 1)
                t.pop()

        dfs(nums, [], length)
        return res


class FSolution(Solution):
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(index):
            print(nums)
            if index == n - 1:
                res.append(nums[:])
                return
            for i in range(index, n):
                # swap index with i
                nums[index], nums[i] = nums[i], nums[index]
                dfs(index + 1)
                nums[index], nums[i] = nums[i], nums[index]  # for backtracking

        dfs(0)
        return res


if __name__ == '__main__':
    print(FSolution().permute(['a', 'b', 'c']))
