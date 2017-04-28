# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/update-bits
@Language: Python
@Datetime: 16-12-21 01:54
'''

class Solution:
    #@param n, m: Two integer
    #@param i, j: Two bit positions
    #return: An integer
    def updateBits(self, n, m, i, j):
        # write your code here
        # if m < 0:
        #     return m
        # if n >= 0:
        #     a = str(bin(n))[2:]
        # else:
        #     a = str(bin(pow(2,31) * 2 - abs(n)))[2:]
        # x = len(a)
        # while x <= 31:
        #     a = '0' + a
        #     x += 1
        # t = i
        # i = 32 - j - 1
        # j = 32 - t
        # b = str(bin(m))[2:]
        # y = len(b)
        # while y < j - i:
        #     b = '0' + b
        #     y += 1
        # a = a[:i] + b + a[j:]
        # if a[0] == '1':
        #     b = int(str(bin(pow(2,31) * 2 - int(a[-31:], 2)))[2:][-31:], 2)
        #     return -b
        # else:
        #     return int(a, 2)
        if m < 0:
            return m
        if n < 0:
            n = pow(2,31) * 2 + n
        a = ~(((1 << j - i + 1) - 1) << i) & n
        b = m << i
        if a | b >= pow(2,31):
            return int(bin(a|b)[-31:],2) - pow(2,31)
        return a | b
        # [-521,0,31,31] fail