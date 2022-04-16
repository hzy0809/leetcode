#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/11 18:59
# @File    : 187_重复的DNA序列.py
# @Software: PyCharm

"""
DNA序列由一系列核苷酸组成，缩写为'A','C','G'和'T'.。

例如，"ACGAATTCCG"是一个 DNA序列 。
在研究 DNA 时，识别 DNA 中的重复序列非常有用。

给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的长度为10的序列(子字符串)。你可以按 任意顺序 返回答案。



示例 1：

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC","CCCCCAAAAA"]
示例 2：

输入：s = "AAAAAAAAAAAAA"
输出：["AAAAAAAAAA"]


提示：

0 <= s.length <= 105
s[i]=='A'、'C'、'G'or'T'

链接：https://leetcode-cn.com/problems/repeated-dna-sequences
"""
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10:
            return []
        res = set()
        result = set()
        for i in range(n - 9):
            r = s[i:i + 10]
            if r in res:
                result.add(r)
            else:
                res.add(r)
        return list(result)


class BSolution(Solution):
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10 or len(s) > 10000:
            return []
        subStrCountDict = {}
        for i in range(0, len(s) - 9):
            subStr = s[i: i + 10]
            subStrCountDict[subStr] = subStrCountDict.get(subStr, 0) + 1
        result = []
        for k, v in subStrCountDict.items():
            if v > 1:
                result.append(k)
        return result
