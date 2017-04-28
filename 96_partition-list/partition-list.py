# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/partition-list
@Language: Python
@Datetime: 16-12-22 02:41
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
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        # write your code here
        a, b, t = ListNode(0), ListNode(0), head
        i, j = a, b
        while t:
            if t.val < x:
                a.next = t
                a = a.next
            else:
                b.next = t
                b = b.next
            t = t.next
        b.next = None
        a.next = j.next
        return i.next
            
        