#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/25 23:34
# @FileName: 10_1_斐波那契数列.py

"""
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
"""


class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007