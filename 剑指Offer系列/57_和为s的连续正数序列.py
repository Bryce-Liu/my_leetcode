#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 23:55
# @FileName: 57_和为s的连续正数序列.py

"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
"""


class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        i, j, result = 1, 2, []  # 预置初始值

        while j <= target // 2 + 1:  # 因为连续正数相加不可能在target的右半部分
            cur_sum = sum(range(i, j+1))  # 计算当前连续数的和
            if cur_sum < target:  # 当小于target时,窗口扩大
                j += 1
            elif cur_sum > target:  # 反之窗口缩小
                i += 1
            else:
                result.append(range(i, j+1))  # 如果命中则将结果添加到result
                j += 1  # 窗口移动
        return result