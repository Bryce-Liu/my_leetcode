#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 22:49
# @FileName: 24_反转链表.py

"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        last = None
        while current:
            tmp = current.next
            current.next = last
            last = current
            current = tmp
        return last