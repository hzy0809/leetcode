#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 13:13
# @Author  : hzy
# @File    : 42_接雨水.py
# @Software: PyCharm
"""
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



示例 1：

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9


提示：

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            if height[left] < height[right]:
                a = left
                while height[a] <= height[left] and a < right:
                    result -= height[a] - height[left]
                    a += 1
                left = a
            else:
                a = right
                while height[a] <= height[right] and a > left:
                    result -= height[a] - height[right]
                    a -= 1
                right = a
        return result
