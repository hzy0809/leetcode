#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/23 11:31
# @File    : 64_最小路径和.py
# @Software: PyCharm

"""
给定一个包含非负整数的 mxn网格grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。



示例 1：


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100


链接：https://leetcode-cn.com/problems/minimum-path-sum
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])

        return grid[m - 1][n - 1]


class BSolution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + grid[0][i]

        for j in range(1, m):
            dp[0] = dp[0] + grid[j][0]
            for i in range(1, n):
                dp[i] = min(dp[i], dp[i - 1]) + grid[j][i]

        return dp[-1]


if __name__ == '__main__':
    print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
