#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 13:01
# @Author  : hzy
# @File    : 11_盛最多水的容器.py
# @Software: PyCharm

"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。在坐标内画 n 条垂直线，垂直线 i的两个端点分别为(i,ai) 和 (i, 0) 。找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。



示例 1：



输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为49。
示例 2：

输入：height = [1,1]
输出：1
示例 3：

输入：height = [4,3,2,1,4]
输出：16
示例 4：

输入：height = [1,2,1]
输出：2


提示：

n = height.length
2 <= n <= 3 * 104
0 <= height[i] <= 3 * 104

链接：https://leetcode-cn.com/problems/container-with-most-water
"""
from typing import List


class Solution:
    def maxArea(self, height: list[int]) -> int:
        a = 0
        b = len(height) - 1
        result = 0
        while a < b:
            if result < min(height[a], height[b]) * (b - a):
                result = min(height[a], height[b]) * (b - a)

            if height[a] < height[b]:
                a += 1
            else:
                b -= 1
        return result

    def better_speed(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maxsize = 0

        while left < right:
            f = right - left
            if height[left] < height[right]:
                h = height[left]
                left = left + 1
            else:
                h = height[right]
                right = right - 1
            size = f * h
            if maxsize < size:
                maxsize = size
        return maxsize

    def better_momery(self, height: List[int]) -> int:
        a = 0
        b = len(height) - 1
        result = min(height[a], height[b]) * (b - a)
        while a < b:
            if height[a] < height[b]:
                i = a
                while i < b and height[i] <= height[a]:
                    i += 1
                a = i
            else:
                i = b
                while i > a and height[i] <= height[b]:
                    i -= 1
                b = i
            result = max(result, min(height[a], height[b]) * (b - a))
        return result
