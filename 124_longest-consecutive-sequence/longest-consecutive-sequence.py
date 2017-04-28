# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/longest-consecutive-sequence
@Language: Python
@Datetime: 16-12-31 12:03
'''

class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        # write your code here
        if not len(num):
            return 0
        num.sort()
        ma = 0
        le = 0
        sus = num[0]
        for i in num:
            if i == sus - 1:
                continue
            if i == sus:
                le += 1
                sus += 1
            else:
                sus = i + 1
                le = 1
            ma = max(le, ma)
        return ma