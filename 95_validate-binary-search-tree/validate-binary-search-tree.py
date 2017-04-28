# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/validate-binary-search-tree
@Language: Python
@Datetime: 16-12-23 17:01
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
    @return: True if the binary tree is BST, or false
    """  
    def isValidBST(self, root):
        # write your code here
        if not root:
            return True
        # return self.check(root.left, max = root.val) and self.check(root.right, min = root.val)
        return self.check(root.left, root.val, None) and self.check(root.right, None, root.val)
    
    
    # def check(self, root, max = None, min = None):
    def check(self, root, max, min):
        if not root:
            return True
        if root.val == max or root.val == min:
            return False
        x, y = True, True
        if min and root.val < min:
            x = False
        if max and root.val > max:
            y = False
        m = x and y
        # if root.left:
        #     print 'left',val, root.val, root.left.val
        # if root.right:
        #     print 'right',val, root.val, root.right.val
        l = self.check(root.left, root.val, min)
        r = self.check(root.right, max, root.val)
        # print root.val, l, r, m
        return l and r and m
        
            