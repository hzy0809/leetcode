#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/11 18:06
# @Author  : hzy
# @File    : 15_三数之和.py
# @Software: PyCharm

"""
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。



示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]


提示：

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

链接：https://leetcode-cn.com/problems/3sum
"""
# from bisect import bisect
from collections import defaultdict
import bisect


class Solution:
    def threeSum(self, nums: list([int])) -> list(list([int])):
        """
        :param nums:
        :return:
        """
        if len(nums) < 3:
            return []
        result = list()
        nums.sort()  # 排序，保证三数的顺序唯一，防止重复
        length = len(nums)
        for first in range(length - 2):
            if first > 0 and nums[first] == nums[first - 1]:  # 跳过相同的元素，防止重复
                continue
            if nums[first] > 0:
                break
            target = - nums[first]  # 将三数之和转换为两数之和
            third = length - 1
            for second in range(first + 1, length - 1):
                if second > first + 1 and nums[second] == nums[second - 1]:  # 跳过相同的元素
                    continue
                while second < third and nums[second] + nums[third] > target:  # 第三个数从高到低遍历
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    result.append([nums[first], nums[second], nums[third]])

                    bisect

        return result

    def fatest(self, nums: list([int])) -> list(list([int])):
        res = []
        if len(nums) < 3:
            return []
        dd = defaultdict(int)
        for i in nums:
            dd[i] += 1
        val = sorted(dd)

        for i, num in enumerate(val):
            # 处理重复数据
            if dd[num] > 1:
                if num == 0 and dd[num] > 2:
                    res.append([0, 0, 0])
                if num != 0 and -2 * num in dd:
                    res.append([num, num, -2 * num])

            if num < 0:
                reverse = -num

                # 确定second的边界，大于等于target-最大值，小于等于target//2
                left = bisect.bisect_left(val, reverse - val[-1], i + 1)
                right = bisect.bisect_right(val, reverse // 2, left)

                # 已经排除重复的值
                for secondnum in val[left:right]:
                    thirdnum = reverse - secondnum
                    if thirdnum in dd and thirdnum != secondnum:
                        res.append([num, secondnum, thirdnum])
        return res


if __name__ == '__main__':
    s = Solution()
    result = s.fatest([-1,0,1,2,-1,-4])
    print(result)
