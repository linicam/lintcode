# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/subsets
@Language: Python
@Datetime: 16-12-26 12:08
'''

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    res = [[]]
    a = []
    def subsets(self, S):
        # write your code here
        if not len(S):
            return [[]]
        le = len(S);
        self.getA(0, le, S);
        for i in self.res:
            i.sort()
        return self.res;
        
    
    def getA(self, x, le, S):
        if x >= le:
            return
        for i in range(x, le):
            self.a.append(S[i])
            self.res.append(self.a[:])
            self.getA(i + 1, le, S)
            self.a.pop()