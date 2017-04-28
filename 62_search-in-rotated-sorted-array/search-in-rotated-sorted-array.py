# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/search-in-rotated-sorted-array
@Language: Python
@Datetime: 16-12-20 23:14
'''

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        # try:
        #     t = A.index(target)
        #     return t
        # except:
        #     return -1
        if not len(A):
            return -1
        i = 0
        j = len(A) - 1
        if A[j] == target:
            return j
        while i <= j:
            mid = (i + j) / 2
            if A[mid] == target:
                return mid
            elif i == j:
                return -1
            if A[mid] > A[i]:
                if A[i] < target and A[mid] > target:
                    j = mid
                elif A[i] == target:
                    return i
                else:
                    i = mid + 1
            elif A[mid] < A[i]:
                if A[j] > target and A[mid] < target:
                    i = mid + 1
                elif A[j] == target:
                    return j
                else:
                    j = mid
            else:
                i = mid + 1
        # return  -1 if A[0] != target else 0