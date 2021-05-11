#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 19:30
# @Author  : hzy
# @File    : 32_最长有效括号.py
# @Software: PyCharm

"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

 

示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0


提示：

0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'

链接：https://leetcode-cn.com/problems/longest-valid-parentheses
"""


class Solution:
    # 动态规划
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = 2 if i - 2 < 0 else dp[i - 2] + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - 2 - dp[i - 1]]
        return max(dp)
