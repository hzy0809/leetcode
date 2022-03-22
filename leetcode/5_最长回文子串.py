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
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            if i > 0:
                dp[i][i - 1] = True
            if i < n - 1:
                dp[i][i + 1] = True
        length = 1
        begin = 0
        current = True
        current1 = True
        temp = False
        for l in range(2, n + 1):
            if not current and not current1:
                break
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j]:
                    if l > length:
                        begin = i
                        length = l
                    temp = True
            current, current1, temp = current1, temp, False

        return s[begin:begin + length]


class BestSolution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        # 保证下方都为不完全的回文字符串,循环终止条件
        s = '#' + s + '/'

        prv = 1
        ans = 0
        ansl = ansr = None
        print(s)
        for i in range(1, len(s)):
            if s[i] != s[prv]:
                # 以prv为中心扩展
                l, r = prv - 1, i
                while s[l] == s[r]:
                    l -= 1
                    r += 1
                if r - l - 1 >= ans:
                    ans = r - l - 1
                    ansl = l + 1
                    ansr = r
                prv = i
        return s[ansl:ansr]


if __name__ == '__main__':
    print(BestSolution().longestPalindrome('abc'))
