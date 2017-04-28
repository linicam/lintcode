# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/flip-bits
@Language: Python
@Datetime: 16-12-20 23:31
'''

class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        # c = str(bin(abs(a) ^ abs(b)))[2:]
        if a < 0 and b > 0:
            c = str(bin((-a - 1) ^ b))[2:]
        elif a > 0 and b < 0:
            c = str(bin(a ^ (-b - 1)))[2:]
        else:
            c = str(bin(a ^ b))[2:]
        count = 0
        for i in c:
            if int(i) == 1:
                count += 1
        if a * b < 0:
            count = 32 - count
        return count