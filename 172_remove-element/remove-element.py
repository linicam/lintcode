# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/remove-element
@Language: Python
@Datetime: 16-12-19 21:58
'''

class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        i = 0
        while i < len(A):
            if A[i] == elem:
                A.pop(i)
                i -= 1
            i += 1
        l = len(A)
        return l