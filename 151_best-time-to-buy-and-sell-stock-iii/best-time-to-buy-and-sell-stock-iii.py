# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iii
@Language: Python
@Datetime: 17-03-30 10:24
'''

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        n = len(prices)
        if n <= 1:
            return 0
        p1 = [0] * n
        p2 = [0] * n
        
        minV = prices[0]
        for i in range(1,n):
            minV = min(minV, prices[i]) 
            # print minV, p1[i-1],prices[i] - minV
            p1[i] = max(p1[i - 1], prices[i] - minV)
        # print p1
        
        maxV = prices[-1]
        for i in range(n-2, -1, -1):
            maxV = max(maxV, prices[i])
            # print maxV, p2[i-1],prices[i] - maxV
            p2[i] = max(p2[i + 1], maxV - prices[i])
        # print p2
        res = 0
        for i in range(n):
            res = max(res, p1[i] + p2[i])
        return res