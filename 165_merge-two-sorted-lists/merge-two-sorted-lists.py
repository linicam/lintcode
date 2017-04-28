# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/merge-two-sorted-lists
@Language: Python
@Datetime: 16-12-22 02:07
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
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        if l1.val <= l2.val:
            start = l1
            l1 = l1.next
        else:
            start = l2
            l2 = l2.next
        head = start
        while l1 != None and l2 != None:
            # print l1.val, l2.val, start.val, head.val
            if l1.val <= l2.val:
                start.next, l1 = l1, l1.next
            else:
                start.next, l2 = l2, l2.next
            start = start.next
        if l1 == None:
            start.next = l2
        else:
            start.next = l1
        return head
                