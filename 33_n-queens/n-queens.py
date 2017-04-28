# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/n-queens
@Language: Python
@Datetime: 16-12-27 10:04
'''

class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    res = []
    def solveNQueens(self, n):
        # write your code here
        num = [i for i in range(n)]
        if not len(num):
            return [[]]
        self.permuteCore(num, 0)
        return self.res
            
    def permuteCore(self, num, start):
        if start == len(num):
            self.buildRes(num)
        for i in range(start, len(num)):
            num[start], num[i] = num[i], num[start]
            if self.checkQueen(num, start):
                self.permuteCore(num, start + 1)
            num[start], num[i] = num[i], num[start]
            
    def checkQueen(self, num, tar):
        res = True
        for i in range(tar):
            if abs(tar - i) == abs(num[tar] - num[i]):
                res = False
        return res

    def buildRes(self, n):
        num = n[:]
        l = len(num)
        for i in range(l):
            num[i] = '.' * num[i] + 'Q' + '.' * (l - num[i] - 1)
        self.res.append(num)