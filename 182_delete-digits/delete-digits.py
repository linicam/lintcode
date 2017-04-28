# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/delete-digits
@Language: Python
@Datetime: 16-12-21 11:17
'''

class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write you code here
        t = len(A) - k
        index = 0
        res = ''
        while t > 0:
            min = 10
            # print 'start'
            for i in range(len(A) - t + 1):
                if int(A[i]) < min:
                    min = int(A[i])
                    index = i
            res += A[index]
            k -= index
            start = index + 1
            A = A[index + 1:]
            t = len(A) - k
            # print index, res, A, t
        while res[0] == '0':
            res = res[1:]
        return res
                    