#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: 479_最大回文数乘积.py
# @time: 2022/4/16 13:54

"""
给定一个整数 n ，返回 可表示为两个 n位整数乘积的 最大回文整数 。因为答案可能非常大，所以返回它对 1337 取余 。



示例 1:

输入：n = 2
输出：987
解释：99 x 91 = 9009, 9009 % 1337 = 987
示例 2:

输入： n = 1
输出： 9


提示:

1 <= n <= 8

链接：https://leetcode-cn.com/problems/largest-palindrome-product
"""


class Solution:
    def largestPalindrome(self, n: int) -> int:
        upper = 10 ** n - 1
        if n == 1:
            return 9
        for x in range(upper, 1, -1):
            l, r = x, x
            while r:
                l = l * 10 + r % 10
                r = r // 10
            # print(l)
            r = upper
            while r * r >= l:
                if l % r == 0:
                    return l % 1337
                r -= 1
