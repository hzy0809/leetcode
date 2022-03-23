#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/23 15:36
# @File    : 300_最长递增子序列.py
# @Software: PyCharm
"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。


示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1


提示：

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


进阶：

你能将算法的时间复杂度降低到O(n log(n)) 吗?

链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
"""
import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 转移方程
        # dp[i]=max(dp[j])+1,其中0≤j<i且num[j]<num[i]
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class CupiditySolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            elif nums[i] < dp[-1]:
                index = bisect.bisect_left(dp, nums[i])
                dp[index] = nums[i]
        return len(dp)


class SCupiditySolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            elif nums[i] < dp[-1]:
                index = self.search(dp, nums[i])
                dp[index] = nums[i]
        return len(dp)

    @staticmethod
    def search(dp, x):
        left = 0
        right = len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < x:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    print(SCupiditySolution().lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]))
    # print(SCupiditySolution().search([2, 5, 6], 4))
