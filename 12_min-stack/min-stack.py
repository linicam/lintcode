# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/min-stack
@Language: Python
@Datetime: 17-01-01 13:49
'''

class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.ele = []

    def push(self, number):
        # write yout code here
        self.ele.append(number)

    def pop(self):
        # pop and return the top item in stack
        return self.ele.pop(len(self.ele) - 1)

    def min(self):
        # return the minimum number in stack
        return min(self.ele)
        