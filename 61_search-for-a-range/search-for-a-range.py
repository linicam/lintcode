# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/search-for-a-range
@Language: Python
@Datetime: 16-12-20 12:50
'''

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not len(A):
            return [-1,-1]
        i = 0
        j = len(A)
        while i < j:
            mid = (i + j) / 2
            if A[mid] < target:
                i = mid + 1
            elif A[mid] > target:
                j = mid
            else:
                t = mid
                while t - 1 >= 0 and A[t - 1] == target:
                    t -= 1
                while mid + 1 < len(A) and A[mid + 1] == target:
                    mid += 1
                return [t, mid]
        return [-1, -1]
        