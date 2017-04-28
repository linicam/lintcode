# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/balanced-binary-tree
@Language: Python
@Datetime: 16-12-23 12:14
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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        def isB(root):
            if not root:
                return 0
            left = isB(root.left)
            right = isB(root.right)
            if abs(left - right) > 1 or left == -1 or right == -1:
                return -1
            return 1 + max(left, right)
        return isB(root) != -1
            