# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/convert-sorted-list-to-balanced-bst
@Language: Python
@Datetime: 16-12-22 11:40
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        if not head.next.next:
            root = TreeNode(head.val)
            root.right = TreeNode(head.next.val)
            return root
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return self.build(a)
            
    def build(self, list):
        if not list:
            return
        l = len(list)
        root = TreeNode(list[l / 2])
        root.left = self.build(list[:l / 2])
        root.right = self.build(list[l / 2 + 1:])
        return root
        
