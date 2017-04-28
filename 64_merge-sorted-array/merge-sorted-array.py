# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/merge-sorted-array
@Language: Python
@Datetime: 16-12-19 22:22
'''

class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        for i in range(m, m+n):
            A[i] = B[i-m]
        A.sort()