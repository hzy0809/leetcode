#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/23 15:17
# @File    : 118_杨辉三角.py
# @Software: PyCharm
"""
给定一个非负整数numRows，生成「杨辉三角」的前numRows行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。





示例 1:

输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
示例2:

输入: numRows = 1
输出: [[1]]


提示:

1 <= numRows <= 30


链接：https://leetcode-cn.com/problems/pascals-triangle
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows + 1):
            temp = [1] * i
            for j in range(1, i - 1):
                temp[j] = result[i - 2][j] + result[i - 2][j - 1]
            result.append(temp)
        return result


if __name__ == '__main__':
    print(Solution().generate(10))
