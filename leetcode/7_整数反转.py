#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 18:42
# @Author  : hzy
# @File    : 7_整数反转.py
# @Software: PyCharm
"""
给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围[−231, 231− 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。


示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0


提示：

-231 <= x <= 231 - 1

链接：https://leetcode-cn.com/problems/reverse-integer
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            str_re = str(x)[::-1]
        elif x == 0:
            return 0
        else:
            str_re = str(x)[1:]
            str_re = "-" + str_re[::-1]
        result = int(str_re)
        if (-2 ** 31) <= result <= (2 ** 31 - 1):
            return result
        else:
            return 0
