# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/search-insert-position
@Language: Python
@Datetime: 16-12-20 00:31
'''

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        i = 0
        j = len(A) - 1
        while i < j:
            mid = (i + j) / 2
            if A[mid] < target:
                i = mid + 1
            elif A[mid] > target:
                j = mid
            else:
                return mid
        return len(A) if len(A) > 1 and target > A[len(A) - 1] else i