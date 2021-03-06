#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/15 09:39
# @FileName: 11_旋转数组的最小数字.py


"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
"""


class Solution:
    def minArray(self, numbers) -> int:
        if len(numbers) == 1:
            return numbers[0]
        for i in range(1, len(numbers)):
            if numbers[i] < numbers[i-1]:
                return numbers[i]
        return numbers[0]
