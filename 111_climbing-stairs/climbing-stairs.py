# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/climbing-stairs
@Language: Python
@Datetime: 16-12-27 22:39
'''

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if not n:
            return 1
        if n == 1:
            return 1
        a, b = 1, 2
        while n > 2:
            a, b = b, a + b
            n -= 1
        return b
