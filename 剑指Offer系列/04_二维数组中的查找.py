#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 23:40
# @FileName: 04_二维数组中的查找.py


"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。

链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
"""


class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix and matrix[0]:  # 当矩阵有数据时才计算
            row, column = len(matrix) - 1, len(matrix[0]) - 1
            i, j = row, 0
            # 令(i,j)的坐标位于左下角,那么此时它右边的数据都比它大, 上边的数据都比它小
            # 因此有(i,j)对应的元素大于target时, i-=1; 反之j+=1
            while i >= 0 and j <= column:  # 限定边界
                if matrix[i][j] > target:
                    i -= 1
                elif matrix[i][j] < target:
                    j += 1
                else:
                    return True
        return False
