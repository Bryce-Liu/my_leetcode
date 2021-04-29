#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 23:18
# @FileName: 06_从尾到头打印链表.py

"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

连接:https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        # 直接通过递归返回
        return self.reversePrint(head.next) + [head.val] if head else []


class Solution2(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        # 遍历链表后反转结果
        stack = []
        node = head
        while node:
            stack.append(node.val)
            node = node.next
        return stack[::-1]