#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/25 12:50
# @Author  : hzy
# @File    : 209_长度最小的子数组.py
# @Software: PyCharm

"""
给定一个含有n个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组[numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。



示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组[4,3]是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0


提示：

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105


进阶：

如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。

链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        slow = 0
        fast = 0
        n = len(nums)
        result = n
        while fast < n or total > target:
            while total < target and fast < n:
                total += nums[fast]
                fast += 1
            while total >= target and slow < n:
                total -= nums[slow]
                slow += 1
            result = min(result, fast - slow + 1)
            if result == 1:
                break
        if slow == 0:
            result = 0
        return result

    def better(self, s: int, nums: List[int]) -> int:
        """
        双指针
        """
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            end += 1
            while total >= s:
                ans = min(ans, end - start)
                total -= nums[start]
                start += 1

        return 0 if ans == n + 1 else ans
