# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/subsets-ii
@Language: Python
@Datetime: 17-01-22 00:34
'''

class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    res = [[]]
    a = []
    def subsetsWithDup(self, S):
        # write your code here
        if not len(S):
            return [[]]
        le = len(S);
        S.sort()
        self.getA(0, le, S);
        for i in self.res:
            i.sort()
        return self.res;
        
    
    def getA(self, x, le, S):
        if x >= le:
            return
        for i in range(x, le):
            if i > x and S[i] == S[i-1]:
                continue
            self.a.append(S[i])
            self.res.append(self.a[:])
            self.getA(i + 1, le, S)
            self.a.pop()