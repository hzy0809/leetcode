#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/11 18:45
# @Author  : hzy
# @File    : 43_字符串相乘.py
# @Software: PyCharm
"""
给定两个以字符串形式表示的非负整数num1和num2，返回num1和num2的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1和num2的长度小于110。
num1 和num2 只包含数字0-9。
num1 和num2均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

链接：https://leetcode-cn.com/problems/multiply-strings
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        c1 = n1 = len(num1) - 1
        n2 = len(num2) - 1
        while c1 >= 0:
            i = int(num1[c1])
            if i == 0:
                c1 -= 1
                continue
            c2 = n2
            while c2 >= 0:
                j = int(num2[c2])
                if j == 0:
                    c2 -= 1
                    continue
                res += i * j * 10 ** (n1 + n2 - c1 - c2)
                c2 -= 1
            c1 -= 1
        return str(res)

    def better(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        m = len(num1)
        n = len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            if x == 0:
                continue
            for j in range(n - 1, -1, -1):
                res[i + j + 1] += x * int(num2[j])

        for i in range(m + n - 1, 0, -1):
            res[i - 1] += res[i] // 10
            res[i] = res[i] % 10

        index = 1 if res[0] == 0 else 0
        return ''.join(str(x) for x in res[index:])
