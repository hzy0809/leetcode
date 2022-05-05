#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 16:24
# @File    : 713_乘积小于K的子数组.py
# @Software: PyCharm
"""
给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。


示例 1：

输入：nums = [10,5,2,6], k = 100
输出：8
解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
示例 2：

输入：nums = [1,2,3], k = 0
输出：0


提示:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106

链接：https://leetcode-cn.com/problems/subarray-product-less-than-k
"""
from collections import deque
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        a = deque()
        res = 0
        pre = 1
        for num in nums:
            temp = pre * num
            while temp >= k and a:
                temp //= a.popleft()
            if temp < k:
                res += len(a) + 1
                a.append(num)
                pre = temp
            else:
                pre = 1
        return res


class BSolution(Solution):
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, prod, i = 0, 1, 0
        for j, num in enumerate(nums):
            prod *= num
            while i <= j and prod >= k:
                prod //= nums[i]
                i += 1
            ans += j - i + 1
        return ans


if __name__ == '__main__':
    print(Solution().numSubarrayProductLessThanK([10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19))
