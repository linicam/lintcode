# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/combination-sum
@Language: Python
@Datetime: 16-12-25 08:18
'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    r = []
    def combinationSum(self, candidates, target):
        # write your code here
        candidates.sort()
        self.getr(candidates, target, 0, [])
        t = {}
        a = self.r[:]
        for i in range(len(a)):
            a[i] = self.r[i][:]
            for j in range(len(a[i])):
                a[i][j] = str(a[i][j])
            a[i] = ','.join(a[i])
        i = 0
        while i < len(a):
            p = a[i]
            if not p in t:
                t[p] = True
            else:
                self.r.pop(i)
                a.pop(i)
                i -= 1
            i += 1
        return self.r
        
    def getr(self, l, tar, start, res):
        if not tar:
            self.r.append(res)
            return
        for i in range(start, len(l)):
            a = []
            a.extend(res)
            if l[i] > tar:
                break
            a.append(l[i])
            self.getr(l, tar-l[i], i, a)