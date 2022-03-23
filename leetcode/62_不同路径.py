#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/23 10:45
# @File    : 62_不同路径.py
# @Software: PyCharm
"""
一个机器人位于一个 m x n网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？



示例 1：


输入：m = 3, n = 7
输出：28
示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
示例 3：

输入：m = 7, n = 3
输出：28
示例 4：

输入：m = 3, n = 3
输出：6


提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 109

链接：https://leetcode-cn.com/problems/unique-paths
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = [[1] * m for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                dp[j][i] = dp[j - 1][i] + dp[j][i - 1]

        return dp[n - 1][m - 1]


class BSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                # dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
                # 本轮的值     本轮上一个值     上一轮的值
                dp[j] += dp[j - 1]
        return dp[n - 1]


if __name__ == '__main__':
    print((BSolution().uniquePaths(m=7, n=3)))
