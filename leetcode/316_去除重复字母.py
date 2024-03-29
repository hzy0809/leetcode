#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 13:13
# @Author  : hzy
# @File    : 316_去除重复字母.py
# @Software: PyCharm
"""
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同

示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"


提示：

1 <= s.length <= 104
s 由小写英文字母组成

链接：https://leetcode-cn.com/problems/remove-duplicate-letters
"""
import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        栈
        :param s:
        :return:
        """
        s_counter = collections.Counter(s)
        stack = []
        seen = set()
        for c in s:
            if c not in seen:
                while stack and stack[-1] > c and s_counter[stack[-1]] > 0:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
            s_counter[c] -= 1

        return ''.join(stack)
