# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/strstr
@Language: Python
@Datetime: 16-12-19 05:09
'''

class Solution:
    def strStr(self, source, target):
        # write your code here
        try:
            t = source.index(target)
        except:
            return -1
        return t