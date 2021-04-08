#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 13:40
# @Author  : hzy
# @File    : 581_最短无序连续子数组.py
# @Software: PyCharm
"""
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。



示例 1：

输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
示例 2：

输入：nums = [1,2,3,4]
输出：0
示例 3：

输入：nums = [1]
输出：0


提示：

1 <= nums.length <= 104
-105 <= nums[i] <= 105

链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
"""
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        tak = [0]
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                while tak and nums[i] < nums[tak[-1]]:
                    tak.pop()
            else:
                if tak and i == tak[-1] + 1:
                    tak.append(i)
        if tak:
            a = tak[-1]
        else:
            a = -1
        if a == n - 1:
            return 0
        tak = [n - 1]
        for i in range(n - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                while tak and nums[i - 1] > nums[tak[-1]]:
                    tak.pop()
            else:
                if tak and i == tak[-1] - 1:
                    tak.append(i)
        if tak:
            b = tak[-1]
        else:
            b = n
        print(a, b)
        return b - a - 1
