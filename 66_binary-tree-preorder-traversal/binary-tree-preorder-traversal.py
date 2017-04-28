# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/binary-tree-preorder-traversal
@Language: Python
@Datetime: 16-12-23 15:54
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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        res = []
        r = []
        while True:
            while root:
                res.append(root.val)
                r.append(root)
                root = root.left
            while r and not r[len(r) - 1].right:
                r.pop()
            if not r:
                break
            root = r[len(r) - 1].right
            r.pop()
        return res
                
            