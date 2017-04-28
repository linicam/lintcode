# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/jump-game
@Language: Python
@Datetime: 16-12-21 11:28
'''

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        max = A[0]
        i = 1
        while i <= max and i < len(A):
            if i + A[i] > max:
                max = i + A[i]
            i += 1
            # print i, max
        if max >= len(A) - 1:
            return True
        else:
            return False