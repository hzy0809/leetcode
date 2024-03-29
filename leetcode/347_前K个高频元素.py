#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/11 14:35
# @File    : 347_前 K 个高频元素.py
# @Software: PyCharm

"""
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。



示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]


提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的


进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n是数组大小。

链接：https://leetcode-cn.com/problems/top-k-frequent-elements
"""

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = Counter(nums)
        return [x[0] for x in result.most_common(k)]
