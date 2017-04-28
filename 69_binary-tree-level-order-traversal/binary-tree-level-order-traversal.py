# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/binary-tree-level-order-traversal
@Language: Python
@Datetime: 16-12-24 11:01
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
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        a = []
        self.build(root, 0, a)
        return a
        
    
    def build(self, root, n, a):
        if not root:
            return
        if len(a) <= n:
            a.append([])
        a[n].append(root.val)
        self.build(root.left, n + 1, a)
        self.build(root.right, n + 1, a)