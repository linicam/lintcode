# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/remove-node-in-binary-search-tree
@Language: Python
@Datetime: 17-01-04 13:21
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    tar = ""
    par = ""
    """
    @param root: The root of the binary search tree.
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """    
    def removeNode(self, root, value):
        # write your code here
        # if not root:
        #     return root
        # if value < root.val:
        #     root.left = self.removeNode(root.left, value)
        # elif value > root.val:
        #     root.right = self.removeNode(root.right, value)
        # else:
        #     if not root.left:
        #         root = root.right
        #     elif not root.right:
        #         root = root.left
        #     else:
        #         t = root.left
        #         while t.right:
        #             t = t.right
        #         root.val = t.val
        #         root.left = self.removeNode(root.left, t.val)
        # return root
        
        self.findt(root, None, value)
        if isinstance(self.tar, TreeNode):
            tmp = self.tar
            if self.tar.left:
                t = self.tar.left
                while t.right:
                    tmp = t
                    t = t.right
                if tmp != self.tar: # ä¸å ä¼å¯¼è´ä¸¢å¤±
                    tmp.right = t.left # tmp.right = Noneéè¯¯ï¼ä¸¢å¤±tçå­æ 
                t.right = self.tar.right
                if t != self.tar.left: # ä¸å ä¼èªèº«æåèªèº«
                    t.left = self.tar.left
            elif self.tar.right:
                t = self.tar.right
                while t.left:
                    tmp = t
                    t = t.left
                if tmp != self.tar:
                    tmp.left = t.right
                if t != self.tar.right:
                    t.right = self.tar.right
            else:
                t = None
            if isinstance(self.par, TreeNode):
                # print 'par'
                if self.par.left == self.tar:
                    self.par.left = t
                else:
                    self.par.right = t
        return root if self.tar != root else t
            
        
    def findt(self, root, par, val):
        if not root:
            return
        if root.val == val:
            self.tar = root
            self.par = par
            return
        self.findt(root.left, root, val)
        if isinstance(self.tar, TreeNode):
            return
        self.findt(root.right, root, val)    