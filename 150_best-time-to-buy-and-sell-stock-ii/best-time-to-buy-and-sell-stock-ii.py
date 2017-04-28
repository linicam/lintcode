# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-ii
@Language: Python
@Datetime: 17-01-21 23:37
'''

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if len(prices) < 2:
            return 0
        i = 0
        while i + 1 < len(prices) and prices[i + 1] < prices[i]:
            i += 1
        start = i
        sum = 0
        i += 1
        while i < len(prices):
            while i + 1 < len(prices) and prices[i] == prices[i + 1]:
                prices.pop(i)
            if i + 1 < len(prices) and prices[i] > prices[i - 1] and prices[i] > prices[i + 1]:
                sum += prices[i] - prices[start]
            if i + 1 < len(prices) and prices[i] < prices[i - 1] and prices[i] < prices[i + 1]:
                start = i
            i += 1
        if prices[i - 1] > prices[i - 2]:
            sum += prices[i - 1] - prices[start]
        return sum
        
        
        # total = 0
        # low, high = sys.maxint, sys.maxint
        # for x in prices:
        #     if x > high:
        #         high = x
        #     else:
        #         total += high - low
        #         high, low = x, x
        # return total + high - low
                