# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/rotate-list
@Language: Python
@Datetime: 16-12-22 03:20
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        # write your code here
        tar, cur = head, ListNode(0)
        cur.next = head
        if not head or not head.next or k == 0:
            return head
        for i in range(1, k):
            tar = tar.next
            if i < k - 1 and not tar:
                # print k, i
                k = k % i
                tar = head
                for j in range(1, k):
                    tar = tar.next
                break
        if k == 0:
            return head
        # print tar.val
        while tar.next != None:
            tar = tar.next
            cur = cur.next
        h = cur.next
        cur.next = None
        tar.next = head
        return h
