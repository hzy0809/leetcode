#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 18:35
# @Author  : hzy
# @File    : 9_回文数.py
# @Software: PyCharm

"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。



示例 1：

输入：x = 121
输出：true
示例2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。
示例 4：

输入：x = -101
输出：false

链接：https://leetcode-cn.com/problems/palindrome-number
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # t = 0
        # if x >= 0:
        #     c = x
        #     while c != 0:
        #         pop = c % 10
        #         c //= 10
        #         t = t * 10 + pop
        #     return True if t == x else False
        # return False
        if x < 0:
            return False
        s = str(x)
        return s[::-1] == s
