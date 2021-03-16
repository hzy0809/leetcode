#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/12 12:46
# @Author  : hzy
# @File    : 172_阶乘后的零.py
# @Software: PyCharm

"""
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释:3! = 6, 尾数中没有零。
示例2:

输入: 5
输出: 1
解释:5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为O(logn)。

链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n >= 5:
            n = n // 5
            result += n
        return result
