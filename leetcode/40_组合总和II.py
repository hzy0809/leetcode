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
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ct = Counter(candidates)
        temp = sorted(ct)
        length = len(temp)

        def combination(res: list, index: int = 0):

            if index >= length:
                return
            num = temp[index]
            r = res[:]
            s = sum(res)
            for i in range(ct[num] + 1):
                if i != 0:
                    r.append(num)
                    s += num
                if s == target:
                    ans.append(r[:])
                    break
                elif s < target:
                    combination(r, index + 1)
                else:
                    break

        combination([])
        return ans


class FSolution(Solution):
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                if candidates[index] > residue:
                    break

                if index > begin and candidates[index - 1] == candidates[index]:
                    continue

                path.append(candidates[index])
                dfs(index + 1, path, residue - candidates[index])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res


if __name__ == '__main__':
    print(FSolution().combinationSum2([2, 5, 2, 1, 2], 5))
