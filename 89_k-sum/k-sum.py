# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/k-sum
@Language: Python
@Datetime: 17-02-20 13:50
'''

class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        # write your code here
        s = [[0] * (target + 1) for j in range(k + 1)]
        s[0][0] = 1
        for i in range(len(A)):
            for j in range(k, 0, -1):
                for x in range(target, A[i] - 1, -1):
                    s[j][x] = s[j - 1][x - A[i]] + s[j][x]
        return s[k][target]