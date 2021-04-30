#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 00:00
# @FileName: 05_替换空格.py


"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"

链接:https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
"""

class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for c in s:
            if c == " ":
                result.append("%20")
            else:
                result.append(c)
        return "".join(result)