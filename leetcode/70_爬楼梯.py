#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/23 14:39
# @File    : 70_爬楼梯.py
# @Software: PyCharm
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？



示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶


提示：

1 <= n <= 45

链接：https://leetcode-cn.com/problems/climbing-stairs/
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        n_2 = 1
        n_1 = 2
        for _ in range(2, n):
            n_1, n_2 = n_1 + n_2, n_1
        return n_1
