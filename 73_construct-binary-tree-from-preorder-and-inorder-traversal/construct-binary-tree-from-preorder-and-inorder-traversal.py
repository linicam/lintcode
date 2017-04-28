# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/construct-binary-tree-from-preorder-and-inorder-traversal
@Language: Python
@Datetime: 16-12-23 19:17
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
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        return self.build(preorder, inorder, 0, 0, len(preorder) - 1)
    
    
    def build(self, pre, ino, i, start, end):
        if start > end:
            return None
        node = TreeNode(pre[i])
        t = ino.index(pre[i], start)
        node.left = self.build(pre, ino, i + 1, start, t - 1)
        node.right = self.build(pre, ino, i + 1 + t - start, t + 1, end)
        return node