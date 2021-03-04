#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 12:58
# @Author  : hzy
# @File    : 56_合并区间.py
# @Software: PyCharm


"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。



示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。


提示：

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

链接：https://leetcode-cn.com/problems/merge-intervals
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1] < intervals[i][1]:
                res[-1][1] = intervals[i][1]
            elif intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
        return res


if __name__ == '__main__':
    s = Solution()
    s.merge([[1, 2]])
