# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/ugly-number-ii
@Language: Python
@Datetime: 17-01-01 17:43
'''

class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        res = [1,2,3]
        if n == 1:
            return 1
        i2 = 1
        i3 = 1
        i5 = 0
        while len(res) < n:
            m2 = res[i2] * 2
            m3 = res[i3] * 3
            m5 = res[i5] * 5
            newM = min(m2, m3, m5)
            res.append(newM)
            while res[i2] * 2 <= newM:
                i2 += 1
            while res[i3] * 3 <= newM:
                i3 += 1
            while res[i5] * 5 <= newM:
                i5 += 1
        # print res
        return res[n - 1]
        

