#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 13:04
# @Author  : hzy
# @File    : 763_划分字母区间.py
# @Software: PyCharm

"""
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。



示例：

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。


提示：

S的长度在[1, 500]之间。
S只包含小写字母 'a' 到 'z' 。

链接：https://leetcode-cn.com/problems/partition-labels
"""
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        result = list()
        temp = set()
        end = course = 0
        n = len(S)
        for i in range(n):
            if S[i] not in temp:
                temp.add(S[i])
                a = S.rfind(S[i]) + 1
                if a > end:
                    end = a
            if end == n:
                result.append(end - course)
                break
            if i >= end - 1:
                result.append(end - course)
                course = end
        return result

    def better(self, S: str) -> List[int]:
        end = {}
        for i, ch in enumerate(S):
            end[ch] = i
        s, e, res = 0, 0, []
        for i, ch in enumerate(S):
            e = max(e, end[ch])
            if i == e:
                res.append(e - s + 1)
                s, e = e + 1, e + 1
        return res
