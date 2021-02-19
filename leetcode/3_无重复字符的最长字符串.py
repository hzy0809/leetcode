#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 12:51
# @Author  : hzy
# @File    : 3_无重复字符的最长字符串.py
# @Software: PyCharm

"""
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。



示例1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0


提示：

0 <= s.length <= 5 * 104
s由英文字母、数字、符号和空格组成

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = b = a = 0
        for i in s:
            if i in s[a:b]:
                result = max(result, b - a)
                a += s[a:b].find(i) + 1
            b += 1
        return max(result, b - a)

    def perferSolution(self, s: str) -> int:
        k = -1
        s_dict = dict()
        res = 0

        for i, c in enumerate(s):
            if c in s_dict and s_dict[c] > k:
                k = s_dict[c]
                s_dict[c] = i
            else:
                s_dict[c] = i

                if i - k > res:
                    res = i - k
        return res
