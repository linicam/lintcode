# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/digit-counts
@Language: Python
@Datetime: 17-02-18 01:14
'''

class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
        sum = 0
        for i in range(n + 1):
            j = i
            while j > 0:
                if j % 10 == k:
                    sum += 1
                j //= 10
        return sum + (1 if k == 0 else 0)
                