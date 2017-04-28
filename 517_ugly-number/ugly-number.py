# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/ugly-number
@Language: Python
@Datetime: 17-01-01 17:22
'''

class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        # Write your code here
        if num < 1:
            return False
        while not num % 2:
            num /= 2
        while not num % 3:
            num /= 3
        while not num % 5:
            num /= 5
        return num == 1