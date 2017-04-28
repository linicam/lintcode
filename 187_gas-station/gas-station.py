# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/gas-station
@Language: Python
@Datetime: 16-12-21 04:49
'''

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        res = []
        for i in range(len(gas)):
            res.append(gas[i] - cost[i])
        i = 0
        r = 0
        start = 0
        while i < len(gas) * 2:
            r += res[i % len(gas)]
            if r < 0:
                start = i + 1
                r = 0
            if start >= len(gas):
                return -1
            i += 1
        return start