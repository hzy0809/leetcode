#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/13 17:03
# @File    : 862_和至少为K的最短子数组.py
# @Software: PyCharm
"""
给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回 -1 。

子数组 是数组中 连续 的一部分。



示例 1：

输入：nums = [1], k = 1
输出：1
示例 2：

输入：nums = [1,2], k = 4
输出：-1
示例 3：

输入：nums = [2,-1,2], k = 3
输出：3


提示：

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109


链接：https://leetcode-cn.com/problems/shortest-subarray-with-sum-at-least-k
"""
from typing import List


class OutTimeSolution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            if nums[i] < k:
                dp[0][i] = nums[i]
            else:
                return 1
        for i in range(1, n):
            for j in range(n - i):
                total = dp[i - 1][j] + nums[i + j]
                print(i, j, total)
                if total >= k:
                    return i + 1
                dp[i][j] = total
        return -1


if __name__ == '__main__':
    print(Solution().shortestSubarray([84, -37, 32, 40, 95], 167))
