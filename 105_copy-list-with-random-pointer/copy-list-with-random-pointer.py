# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/copy-list-with-random-pointer
@Language: Python
@Datetime: 16-12-23 05:36
'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return head
        um = {}
        v = []
        p = head
        n = 0
        while p:
            um[p] = n
            n += 1
            v.append(RandomListNode(p.label))
            p = p.next
        for i in range(n - 1):
            v[i].next = v[i + 1]
        p = head
        for i in range(n):
            v[i].random = v[um[p.random]] if p.random else None
            p = p.next
        return v[0]