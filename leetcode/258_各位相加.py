#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/16 13:48
# @Author  : hzy
# @File    : 258_各位相加.py
# @Software: PyCharm
"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

示例:

输入: 38
输出: 2 
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于2 是一位数，所以返回 2。
进阶:
你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？

链接：https://leetcode-cn.com/problems/add-digits
"""


class Solution:
    def addDigits(self, num: int) -> int:
        if not num:
            return num
        n = num % 9
        return n if n else 9
