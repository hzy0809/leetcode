#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 12:29
# @Author  : hzy
# @File    : 20_有效的括号.py
# @Software: PyCharm
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。


示例 1：

输入：s = "()"
输出：true
示例2：

输入：s = "()[]{}"
输出：true
示例3：

输入：s = "(]"
输出：false
示例4：

输入：s = "([)]"
输出：false
示例5：

输入：s = "{[]}"
输出：true


提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成

]链接：https://leetcode-cn.com/problems/valid-parentheses
"""


class Solution:
    def isValid(self, s: str) -> bool:
        sign = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        j = list()
        for i in s:
            if i not in sign:
                j.append(i)
            else:
                if not j or j.pop() != sign[i]:
                    return False
        return not j
