# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/combinations
@Language: Python
@Datetime: 16-12-25 05:49
'''

class Solution:
    """    
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n   
    """
    t = []
    def combine(self, n, k):
        # write your code here  
        l = []
        for i in range(n):
            l.append(i + 1)
        self.sel(l, k, [])
        return self.t
            
            
    def sel(self, l, k, res):
        if not k:
            self.t.append(res)
            return
        for i in range(len(l) - k + 1):
            a = []
            a.extend(res)
            a.append(l[i])
            self.sel(l[i + 1:], k - 1, a)
        