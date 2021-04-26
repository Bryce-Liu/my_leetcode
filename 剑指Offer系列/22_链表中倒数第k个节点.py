#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 23:14
# @FileName: 22_链表中倒数第k个节点.py

"""
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

示例：
给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.

链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node, next_k = head, head
        for _ in range(k):
            next_k = next_k.next  # 让其中一个指针往前走k次
        while next_k:
            node, next_k = node.next, next_k.next  # 当前面的指针指向None时,后面指针对应的就是倒数第k个节点
        return node