#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/16 11:17
# @FileName: 29_顺时针打印矩阵.py


"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字

链接: https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/
"""

class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return []
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = []
        while True:
            for column in range(l, r + 1):
                res.append(matrix[t][column])
            t += 1
            if t > b: break
            for row in range(t, b + 1):
                res.append(matrix[row][r])
            r -= 1
            if l > r: break
            for column in range(r, l - 1, -1):
                res.append(matrix[b][column])
            b -= 1
            if t > b: break
            for row in range(b, t - 1, -1):
                res.append(matrix[row][l])
            l += 1
            if l > r: break
        return res

    def spiralOrder2(self, matrix):
        result = []
        while matrix:
            result += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return result