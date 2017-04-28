# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/best-time-to-buy-and-sell-stock
@Language: Python
@Datetime: 17-03-30 10:20
'''

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not len(prices):
            return 0
        pro = 0
        mi = prices[0]
        for i in prices:
            pro = max(pro, i - mi)
            mi = min(i, mi)
        return pro