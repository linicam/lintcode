# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/wood-cut
@Language: Python
@Datetime: 16-12-20 12:11
'''

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        i = 1
        if not len(L):
            return 0
        L.sort()
        j = L[len(L) - 1]
        # print self.TP(L, 1)
        if self.TP(L, j) >= k:
            return j
        if self.TP(L, i) < k:
            return 0
        while i < j:
            mid = (i + j) / 2
            if self.TP(L, mid) < k:
                j = mid
            elif self.TP(L, mid) >= k:
                i = mid + 1
        return i if self.TP(L, i) == k else i - 1
            
    def TP(self, L, len):
        sum = 0
        for i in L:
            sum += i / len
        return sum
            
            