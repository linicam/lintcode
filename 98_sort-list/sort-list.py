# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/sort-list
@Language: Python
@Datetime: 16-12-22 19:03
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
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if not head or not head.next:
            return head
        l = []
        while head:
            l.append(head)
            head = head.next
        r = self.merge(l[:len(l) / 2], l[len(l) / 2:])
        for x in range(len(r) - 1):
            r[x].next = r[x + 1]
        r[len(r) - 1].next = None
        return r[0]
        
    def merge(self, left, right):
        lm = len(left) / 2
        rm = len(right) / 2
        # print len(left), len(right)
        if not len(left):
            return right
        left = self.merge(left[:lm], left[lm:])
        right = self.merge(right[:rm], right[rm:])
        i, j = 0, 0
        res = []
        while i < len(left) and j < len(right):
            if left[i].val <= right[j].val:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        if i < len(left):
            res.extend(left[i:])
        if j < len(right):
            res.extend(right[j:])
        return res