# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/reorder-list
@Language: Python
@Datetime: 17-01-21 19:33
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
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        a, b, c = head, head, head
        if not head or not head.next or not head.next.next:
            return head
        while c and c.next:
            c = c.next.next
            pre = b
            b = b.next
        if c and not c.next:
            pre = b
            b = b.next
        d = self.reverseLL(b)
        pre.next = None
        while d:
            a.next, d.next, a, d = d, a.next, a.next, d.next
        # while head:
        #     print head.val
        #     head = head.next
        
    def reverseLL(self, head):
        pre = None
        while head:
            head.next, pre, head = pre, head, head.next
        return pre
