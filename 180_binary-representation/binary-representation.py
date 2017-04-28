# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/binary-representation
@Language: Python
@Datetime: 16-12-21 04:37
'''

class Solution:
    #@param n: Given a decimal number that is passed in as a string
    #@return: A string
    def binaryRepresentation(self, n):
        # write you code here
        t = n.split('.')
        r = float('0.' + t[1])
        t = bin(int(t[0]))[2 if n > 0 else 3:] + '.'
        count = 0
        while count < 32:
            if r == 0:
                return t if t[-1:] != '.' else t[:-1]
            elif r >= 0.5:
                r = r * 2 - 1
                t += '1'
            elif r < 0.5:
                t += '0'
                r = r * 2
            count += 1
        return 'ERROR'
            
        