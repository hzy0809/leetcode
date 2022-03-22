#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/22 11:43
# @File    : 34_在排序数组中查找元素的第一个和最后一个位置.py
# @Software: PyCharm
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回[-1, -1]。

进阶：

你可以设计并实现时间复杂度为O(log n)的算法解决此问题吗？


示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]


提示：

0 <= nums.length <= 105
-109<= nums[i]<= 109
nums是一个非递减数组
-109<= target<= 109


链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] == nums[right] == target:
                break
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if nums[left] < target:
                    left += 1
                if nums[right] > target:
                    right -= 1
        return [left, right] if left < right or nums[left] == target else [-1, -1]


class FastSolution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        list_1 = []
        for i in range(len(nums)):
            if nums[i] == target:
                list_1.append(i)
        if not list_1:
            return [-1, -1]
        else:
            res.append(list_1[0])
            res.append(list_1[-1])
            return res
