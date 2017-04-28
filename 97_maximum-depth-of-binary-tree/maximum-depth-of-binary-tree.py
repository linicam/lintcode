# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/maximum-depth-of-binary-tree
@Language: Python
@Datetime: 16-12-23 12:04
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
    @param root: The root of binary tree.
    @return: An integer
    """ 
    
    def maxDepth(self, root):
        # write your code here
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0