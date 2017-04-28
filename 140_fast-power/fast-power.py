# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/fast-power
@Language: Python
@Datetime: 16-12-21 04:25
'''

class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        a = a % b
        if n == 0:
            return 1 % b
        res = 1
        while n != 0:
            if n & 1:
                res = (res * a) % b
            n >>= 1
            a = (a * a) % b
        return res