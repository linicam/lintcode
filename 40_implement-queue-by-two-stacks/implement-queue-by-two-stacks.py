# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/implement-queue-by-two-stacks
@Language: Python
@Datetime: 17-01-01 14:10
'''

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, element):
        self.stack1.append(element)
        self.stack2.insert(0, element)
        # write your code here

    def top(self):
        # write your code here
        # return the top element
        return self.stack1[0]

    def pop(self):
        # write your code here
        # pop and return the top element
        self.stack1.pop(0)
        return self.stack2.pop()
