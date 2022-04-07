#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: 648_单词替换.py
# @time: 2022/4/7 21:01
"""
在英语中，我们有一个叫做词根(root) 的概念，可以词根后面添加其他一些词组成另一个较长的单词——我们称这个词为继承词(successor)。例如，词根an，跟随着单词other(其他)，可以形成新的单词another(另一个)。

现在，给定一个由许多词根组成的词典 dictionary 和一个用空格分隔单词形成的句子 sentence。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。

你需要输出替换之后的句子。



示例 1：

输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"
示例 2：

输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
输出："a a b c"


提示：

1 <= dictionary.length<= 1000
1 <= dictionary[i].length <= 100
dictionary[i]仅由小写字母组成。
1 <= sentence.length <= 10^6
sentence仅由小写字母和空格组成。
sentence 中单词的总量在范围 [1, 1000] 内。
sentence 中每个单词的长度在范围 [1, 1000] 内。
sentence 中单词之间由一个空格隔开。
sentence没有前导或尾随空格。

链接：https://leetcode-cn.com/problems/replace-words
"""
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        s = []
        s.append(dictionary[0])
        for i in range(1, len(dictionary)):
            if dictionary[i].startswith(dictionary[i - 1]):
                continue
            s.append(dictionary[i])
        sent = sentence.split()
        for i in range(len(sent)):
            for x in s:
                if sent[i].startswith(x):
                    sent[i] = x
                    break
        return ' '.join(sent)


class FSolution(Solution):
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        mapping = {}
        for x in dictionary:
            t = mapping
            for i in range(len(x)):
                if x[i] not in t:
                    t[x[i]] = {}
                t = t[x[i]]
            t['end'] = i
        print(mapping)
        sent = sentence.split()
        for i, w in enumerate(sent):
            temp = mapping
            for j in range(len(w)):
                if w[j] in temp:
                    temp = temp[w[j]]
                else:
                    break
                if 'end' in temp:
                    sent[i] = w[:j + 1]
                    break
        return ' '.join(sent)


if __name__ == '__main__':
    print(FSolution().replaceWords(["cat","bat","rat"],"the cattle was rattled by the battery"))
