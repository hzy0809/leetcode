#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: 53_最大子数组和.py
# @time: 2022/3/22 23:14

"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。



示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组[4,-1,2,1] 的和最大，为6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23


提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104

链接：https://leetcode-cn.com/problems/maximum-subarray
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        temp = res if res >= 0 else 0
        for i in range(1, len(nums)):
            temp = nums[i] + temp
            if temp > res:
                res = temp
            if temp < 0:
                temp = 0

        return res


class DynamicSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        max_item = nums[0]
        for x in nums:
            pre = max(pre + x, x)
            max_item = max(pre, max_item)
        return max_item


if __name__ == '__main__':
    print(DynamicSolution().maxSubArray([-2, -1, -3, -4, -1, -2, -1, -5, -4]))
