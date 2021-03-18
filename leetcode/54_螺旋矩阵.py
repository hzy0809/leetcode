#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/18 12:56
# @Author  : hzy
# @File    : 54_螺旋矩阵.py
# @Software: PyCharm

"""
给你一个 m 行 n 列的矩阵matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。



示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：


输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

链接：https://leetcode-cn.com/problems/spiral-matrix
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return matrix
        res = list()
        while matrix:
            if len(matrix) == 1:
                res.extend(matrix.pop(0))
                break
            if len(matrix[0]) == 1:
                res.extend([x[0] for x in matrix])
                break
            if len(matrix[0]) == 0:
                break
            res.extend(matrix.pop(0))
            for m in matrix:
                res.append(m.pop(-1))
            res.extend(matrix.pop(-1)[::-1])
            for m in matrix[::-1]:
                res.append(m.pop(0))

        return res

    def better(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

