# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/insert-node-in-a-binary-search-tree
@Language: Python
@Datetime: 16-12-23 12:23
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
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if not root:
            return node
        t = root
        while t:
            if t.val > node.val:
                if t.left:
                    t = t.left
                else:
                    t.left = node
            elif t.val < node.val:
                if t.right:
                    t = t.right
                else:
                    t.right = node
            else:
                break
        return root