#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/22 16:19
# @File    : dynamic_programming.py
# @Software: PyCharm

"""
爬楼梯
题目
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
  [plaintext]
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
= Example 2:

  [plaintext]
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
Constraints:

1 <= n <= 45
"""

"""
解题思路
// 如果为1，只有1中 // 如果为2，则有 11 或者 2 // 如果为3 111 12 21 // 如果为4 1111 112 121 211 22 // 有两种方式：第一次走一步；第一次走两步。

这一题可以拆分为第一次走1步，第一次走两步。地推公式如下：

dp[i] = dp[i-1] + dp[i-2];
"""


# public int climbStairs(int n) {
#     int[] dp = new int[n+1];
#     dp[0] = 1;
#     dp[1] = 2;
#     for(int i = 2; i < n; i++) {
#         dp[i] = dp[i-1] + dp[i-2];
#     }
#     return dp[n-1];
# }

def climb_stars(n: int):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n - 1]


if __name__ == '__main__':
    print(climb_stars(10))
