#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 18:21
# @Author  : hzy
# @File    : 384_打乱数组.py
# @Software: PyCharm
"""
给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。

实现 Solution class:

Solution(int[] nums) 使用整数数组 nums 初始化对象
int[] reset() 重设数组到它的初始状态并返回
int[] shuffle() 返回数组随机打乱后的结果


示例：

输入
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
输出
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

解释
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]


提示：

1 <= nums.length <= 200
-106 <= nums[i] <= 106
nums 中的所有元素都是 唯一的
最多可以调用 5 * 104 次 reset 和 shuffle

链接：https://leetcode-cn.com/problems/shuffle-an-array
"""
from random import randrange
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # res = []
        # _num = self.nums[:]
        # while _num:
        #     m = len(_num)
        #     i = random.randint(0,m-1)
        #     res.append(_num.pop(i))
        # return res

        # 洗牌法
        res = self.nums[:]
        n = len(res)
        for i in range(n):
            swap_index = randrange(i, n)
            res[i], res[swap_index] = res[swap_index], res[i]
        return res
