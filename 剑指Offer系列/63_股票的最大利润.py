#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 10:30
# @FileName: 63_股票的最大利润.py
# https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest, profit = float("+inf"), 0  # 定义最低价格初始值为无穷大,利润为0

        for price in prices:
            cheapest = min(cheapest, price)  # 获取前n天的最低价
            profit = max(profit, price - cheapest)  # 从前n-1天最大利润和第n天的最大利润中取更大的一项
        return profit