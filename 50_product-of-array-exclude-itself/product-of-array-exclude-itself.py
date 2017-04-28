# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/product-of-array-exclude-itself
@Language: Python
@Datetime: 16-12-19 22:36
'''

class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        D = [0 for x in range(len(A))]
        sum = 1
        for i in range(len(A)):
            sum *= A[i]
            D[i] = sum
        A.reverse()
        sum = 1
        C = [0 for x in range(len(A))]
        for i in range(len(A)):
            sum *= A[i]
            C[i] = sum
        B = [0 for x in range(len(A))]
        for i in range(len(A)):
            if i == 0:
                B[i] = C[len(A) - 2]
            elif i == len(A) - 1:
                B[i] = D[len(A) - 2]
            else:
                B[i] = D[i - 1] * C[len(A) - i - 2]
        if len(B) == 1 and B[0] == 0:
            return [1]
        return B