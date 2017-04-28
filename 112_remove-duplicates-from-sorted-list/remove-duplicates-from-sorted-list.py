# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/remove-duplicates-from-sorted-list
@Language: Python
@Datetime: 16-12-22 02:14
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
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        t = head
        while t and t.next:
            if t.val == t.next.val:
                t.next = t.next.next
            else:
                t = t.next
        return head