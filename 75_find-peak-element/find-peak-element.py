# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/find-peak-element
@Language: Python
@Datetime: 16-12-20 12:29
'''

class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        if not len(A):
            return -1
        i = 0
        j = len(A) - 1
        while i < j - 1:
            mid = (i + j) / 2
            if A[mid] <= A[mid + 1]:
                i = mid
            elif A[mid] <= A[mid - 1]:
                j = mid
            else:
                return mid
        return -1