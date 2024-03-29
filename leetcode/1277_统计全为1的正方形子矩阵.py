#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: 1277_统计全为1的正方形子矩阵.py
# @time: 2022/3/24 22:04

"""
给你一个m * n的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。



示例 1：

输入：matrix =
[
 [0,1,1,1],
 [1,1,1,1],
 [0,1,1,1]
]
输出：15
解释： 
边长为 1 的正方形有 10 个。
边长为 2 的正方形有 4 个。
边长为 3 的正方形有 1 个。
正方形的总数 = 10 + 4 + 1 = 15.
示例 2：

输入：matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
输出：7
解释：
边长为 1 的正方形有 6 个。 
边长为 2 的正方形有 1 个。
正方形的总数 = 6 + 1 = 7.


提示：

1 <= arr.length<= 300
1 <= arr[0].length<= 300
0 <= arr[i][j] <= 1

链接：https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones
"""
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = sum(matrix[i][0] for i in range(m)) + sum(matrix[0][i] for i in range(n)) - matrix[0][0]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]:
                    matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]) + 1
                    res += matrix[i][j]
        return res


if __name__ == '__main__':
    print(Solution().countSquares([[0, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1], [1, 0, 1, 0]]))
