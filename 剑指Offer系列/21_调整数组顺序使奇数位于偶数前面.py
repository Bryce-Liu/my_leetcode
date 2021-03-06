#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 15:33
# @FileName: 21_调整数组顺序使奇数位于偶数前面.py


"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分
"""

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        odd, even = [], []
        for n in nums:
            if n % 2 == 1:
                odd.append(n)
            else:
                even.append(n)
        return odd + even

    def exchange2(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] % 2 == 1:
                i += 1
            while i < j and nums[j] % 2 == 0:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums