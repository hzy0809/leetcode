#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/12 14:05
# @File    : 44_通配符匹配.py
# @Software: PyCharm
"""
给定一个字符串(s) 和一个字符模式(p) ，实现一个支持'?'和'*'的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s可能为空，且只包含从a-z的小写字母。
p可能为空，且只包含从a-z的小写字母，以及字符?和*。
示例1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例2:

输入:
s = "aa"
p = "*"
输出: true
解释:'*' 可以匹配任意字符串。
示例3:

输入:
s = "cb"
p = "?a"
输出: false
解释:'?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释:第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例5:

输入:
s = "acdcb"
p = "a*c?b"
输出: false

链接：https://leetcode-cn.com/problems/wildcard-matching
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cs = len(s)
        cp = len(p)
        dp = [[False] * (cs + 1) for _ in range(cp + 1)]
        dp[0][0] = True
        for i, _s in enumerate(p):
            if _s != '*':
                break
            dp[i + 1][0] = True

        for i in range(1, cp + 1):
            for j in range(1, cs + 1):
                if p[i - 1] == s[j - 1] or p[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                if p[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1] or dp[i - 1][j - 1]
        print(dp)
        return dp[cp][cs]


class TOSolution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        elif s and not p:
            return False
        elif not s and p[0] == '*':
            return self.isMatch(s, p[1:])
        elif s and p:
            if p[0] == '*':
                for i in range(len(s) + 1):
                    res = self.isMatch(s[i:], p[1:])
                    if res:
                        return True
            elif p[0] == '?' or p[0] == s[0]:
                return self.isMatch(s[1:], p[1:])
        return False


class DoubleCursorSolution(Solution):
    def isMatch(self, s: str, p: str) -> bool:
        ls = len(s)
        lp = len(p)



if __name__ == '__main__':
    data = dict(s="aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", p="a*******b")
    print(DoubleCursorSolution().isMatch(**data))
