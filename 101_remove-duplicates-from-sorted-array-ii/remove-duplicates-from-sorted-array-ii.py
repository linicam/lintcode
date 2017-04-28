# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/remove-duplicates-from-sorted-array-ii
@Language: Python
@Datetime: 17-01-21 04:04
'''

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        i = 2
        while i < len(A):
            if i > 1 and A[i] == A[i - 2]:
                A.pop(i)
                i -= 1
            i += 1
        return len(A)
          