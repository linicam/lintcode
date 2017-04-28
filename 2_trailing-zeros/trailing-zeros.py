# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/trailing-zeros
@Language: Python
@Datetime: 16-12-19 04:53
'''

class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        t = 1
        count = 0
        while n > pow(5, t):
            count += n / pow(5, t)
            t += 1
        return count