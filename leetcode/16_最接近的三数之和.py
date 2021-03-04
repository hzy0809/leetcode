#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 13:20
# @Author  : hzy
# @File    : 16_最接近的三数之和.py
# @Software: PyCharm

"""
给定一个包括n 个整数的数组nums和 一个目标值target。找出nums中的三个整数，使得它们的和与target最接近。返回这三个数的和。假定每组输入只存在唯一答案。



示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。


提示：

3 <= nums.length <= 10^3
-10^3<= nums[i]<= 10^3
-10^4<= target<= 10^4

链接：https://leetcode-cn.com/problems/3sum-closest
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = 1e7
        for i ,num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            target_1 = target - num
            while left < right:
                if result > abs(nums[right] + nums[left] - target_1):
                    res = nums[right] + nums[left] + num
                    result = abs(nums[right] + nums[left] - target_1)
                if nums[right] + nums[left] == target_1:
                    return target
                elif nums[right] + nums[left] > target_1:
                    right -= 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1
                else:
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return res
