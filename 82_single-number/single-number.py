# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/single-number
@Language: Python
@Datetime: 16-12-21 04:39
'''

class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        # write your code here
        if not len(A):
            return 0
        t = A[0]
        for i in range(1, len(A)):
            t = t ^ A[i]
        return t