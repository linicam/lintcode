# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/search-range-in-binary-search-tree
@Language: Python
@Datetime: 16-12-24 11:38
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):
        # write your code here
        a = []
        self.addt(root, k1, k2, a)
        a.sort()
        return a
        
    def addt(self, root, k1, k2, a):
        if not root:
            return
        if root.val >= k1 and root.val <= k2:
            a.append(root.val)
            self.addt(root.left, k1, k2, a)
            self.addt(root.right, k1, k2, a)
        elif root.val < k1:
            self.addt(root.right, k1, k2, a)
        else:
            self.addt(root.left, k1, k2, a)
        