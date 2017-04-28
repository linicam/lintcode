# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/binary-tree-serialization
@Language: Python
@Datetime: 16-12-24 13:47
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    ind = 0
    arr = []
    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code here
        a = []
        self.se(root, a)
        res = ' '.join(a)
        # print res
        return res

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        self.arr = data.split(' ')
        self.ind = 0
        r = self.de()
        return r
        # write your code here
        
        
    def se(self, root, a):
        if not root:
            a.append('#')
            return
        a.append(str(root.val))
        self.se(root.left, a)
        self.se(root.right, a)
        
    def de(self):
        if self.arr[self.ind] == '#':
            self.ind += 1
            return None
        else:
            root = TreeNode(int(self.arr[self.ind]))
            self.ind += 1
            root.left = self.de()
            root.right = self.de()
            return root