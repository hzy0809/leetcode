#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/22 13:15
# @File    : 5_最长回文子串.py
# @Software: PyCharm
"""
给你一个字符串 s，找到 s 中最长的回文子串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"


提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成


链接：https://leetcode-cn.com/problems/longest-palindromic-substring
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2 or s == s[::-1]:
            return s

        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        # for i in range(n):
        #     dp[i][i] = True

        # 递推开始
        # 先枚举子串长度
        current0 = True
        current1 = True
        temp = False
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            if not current0 and not current1:
                break
            for i in range(0, n - L + 1):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j]:
                    temp = True
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        begin = i
            current0, current1 = current1, temp
            temp = False
        return s[begin:begin + max_len]
