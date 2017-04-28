# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/palindrome-partitioning
@Language: Python
@Datetime: 17-02-18 16:26
'''

class Solution:
    # @param s, a string
    # @return a list of lists of string
    res = []
    def partition(self, s):
        # write your code here
        self.parti(s, [])
        return self.res
        
    def parti(self, s, lis):
        if not len(s):
            self.res.append(lis)
        for i in range(1, len(s) + 1):
            if self.isP(s[:i]):
                self.parti(s[i:], lis + [s[:i]])
        
    def isP(self, s):
        for i in range(len(s) // 2 + 1):
            if(s[i] != s[len(s) - 1 - i]):
                return False
        return True