# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/sqrtx
@Language: Python
@Datetime: 16-12-20 00:28
'''

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        # res = math.sqrt(x)
        # return int(res)
        if x == 0:
            return 0
        i = 1
        j = x
        while i < j:
            mid = (i + j) / 2
            if mid * mid > x:
                j = mid
            elif mid * mid < x:
                i = mid + 1
            else:
                return mid
        return 1 if x < 3 else i - 1