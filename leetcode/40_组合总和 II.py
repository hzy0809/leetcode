#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/25 18:24
# @File    : 40_组合总和 II.py
# @Software: PyCharm
"""
给定一个候选人编号的集合candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。

candidates中的每个数字在每个组合中只能使用一次。

注意：解集不能包含重复的组合。



示例1:

输入: candidates =[10,1,2,7,6,1,5], target =8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
示例2:

输入: candidates =[2,5,2,1,2], target =5,
输出:
[
[1,2,2],
[5]
]


提示:

1 <=candidates.length <= 100
1 <=candidates[i] <= 50
1 <= target <= 30

链接：https://leetcode-cn.com/problems/combination-sum-ii
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

