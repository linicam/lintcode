# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/remove-nth-node-from-end-of-list
@Language: Python
@Datetime: 16-12-22 01:54
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        pre, tar, cur = ListNode(0), head, head
        pre.next = cur
        for i in range(n):
            tar = tar.next
        if tar == None:
            return head.next
        while tar != None:
            tar = tar.next
            pre = cur
            cur = cur.next
        pre.next = cur.next
        return head