# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/reverse-linked-list
@Language: Python
@Datetime: 16-12-22 02:57
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
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        if not head or not head.next:
            return head
        cur = head.next.next
        h = head.next
        h.next = head
        h.next.next = None
        while cur:
            t = cur.next
            cur.next = h
            h = cur
            cur = t
        return h