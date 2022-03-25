#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: 10_正则表达式匹配.py
# @time: 2022/3/24 22:42
"""
给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和'*'的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。


示例 1：

输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
示例 2:

输入：s = "aa", p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例3：

输入：s = "ab", p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。


提示：

1 <= s.length<= 20
1 <= p.length<= 30
s只包含从a-z的小写字母。
p只包含从a-z的小写字母，以及字符.和*。
保证每次出现字符* 时，前面都匹配到有效的字符

链接：https://leetcode-cn.com/problems/regular-expression-matching
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        now_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (now_match and self.isMatch(s[1:], p))
        else:
            return now_match and self.isMatch(s[1:], p[1:])


class DynamicSolution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]


if __name__ == '__main__':
    "mississippi"
    "mis*is*ip*."
    print(Solution().isMatch(s="ab", p=".*..c*"))
