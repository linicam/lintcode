# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/merge-intervals
@Language: Python
@Datetime: 17-04-01 07:35
'''



"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        # write your code here
        if not len(intervals):
            return []
        t = sorted(intervals, self.cmp)
        res = []
        s = t[0].start
        en = t[0].end
        for i in t:
            if i.start <= en:
                en = max(en, i.end)
            else:
                res.append([s, en])
                s = i.start
                en = i.end
        res.append([s, en])
        return res
        
    def cmp(self, a, b):
        if a.start == b.start:
            return a.end - b.end
        else:
            return a.start - b.start