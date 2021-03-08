#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 18:37
# @Author  : hzy
# @File    : 14_最长公共前缀.py
# @Software: PyCharm

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串""。



示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。


提示：

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成

链接：https://leetcode-cn.com/problems/longest-common-prefix
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        if not strs:
            return result
        count = len(strs)
        if count == 1:
            return strs[0]
        length = len(strs[0])
        for i in range(1, length + 1):
            # 使用切片防止index超出
            a = strs[0][:i]
            for j in range(1, count):
                if a != strs[j][:i]:
                    return result
            result = strs[0][:i]
        return result
