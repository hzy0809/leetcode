#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 13:11
# @Author  : hzy
# @File    : 224_基本计算器.py
# @Software: PyCharm


class Solution:
    def calculate(self, s: str) -> int:
        reverse_op = {
            '+': '-',
            '-': '+'
        }
        operator = '+'
        oper_stack = ['+']
        number_stack = []
        s = s.replace(' ', '')
        n = len(s)
        result = 0
        i = -1
        while i < n - 1:
            i += 1
            if s[i].isnumeric():
                number_stack.append(s[i])
                continue
            if number_stack:
                result += int(operator + ''.join(number_stack))
                number_stack.clear()
            if s[i] == '(':
                oper_stack.append(operator)
            elif s[i] == ')':
                oper_stack.pop()
            else:
                operator = s[i] if oper_stack[-1] == '+' else reverse_op[s[i]]
        if number_stack:
            result += int(operator + ''.join(number_stack))
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.calculate("1"))
    print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
    print(s.calculate('6+8'))
    print(s.calculate('-1+2'))
