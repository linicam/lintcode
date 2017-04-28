# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/kth-largest-element
@Language: Python
@Datetime: 17-02-18 01:29
'''

class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        A.sort()
        A.reverse()
        return A[k - 1]