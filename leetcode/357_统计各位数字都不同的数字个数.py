#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/11 10:41
# @File    : 357_统计各位数字都不同的数字个数.py
# @Software: PyCharm
"""
给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10n。


示例 1：

输入：n = 2
输出：91
解释：答案应为除去 11、22、33、44、55、66、77、88、99 外，在 0 ≤ x < 100 范围内的所有数字。 
示例 2：

输入：n = 0
输出：1


提示：

0 <= n <= 8

链接：https://leetcode-cn.com/problems/count-numbers-with-unique-digits
"""

dp = [0] * 10
dp[0] = 1
dp[1] = 9
for i in range(1, 9):
    if not dp[i]:
        dp[i] = dp[i - 1] * (11 - i)
for i in range(1, 9):
    dp[i] = dp[i - 1] + dp[i]


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return dp[n]


class BSolution(Solution):
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        res, cur = 10, 9
        for i in range(n - 1):
            cur *= 9 - i
            res += cur
        return res
