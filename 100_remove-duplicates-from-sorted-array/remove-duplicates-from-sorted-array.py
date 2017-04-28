# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/remove-duplicates-from-sorted-array
@Language: Python
@Datetime: 16-12-19 22:19
'''

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        i = 1
        while i < len(A):
            if i > 0 and A[i] == A[i - 1]:
                A.pop(i)
                i -= 1
            i += 1
        return len(A)
          