# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/o1-check-power-of-2
@Language: Python
@Datetime: 17-01-01 13:43
'''

class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        # t = n & n - 1
        # if t == 0 and n > 0:
        #     return True
        # else:
        #     return False
        return n > 0 and n & (n - 1) == 0