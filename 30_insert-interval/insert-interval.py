# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/insert-interval
@Language: Python
@Datetime: 17-01-25 17:18
'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        if not len(intervals):
            return [newInterval]
        # write your code here
        i = 0
        while i < len(intervals) and intervals[i].start <= newInterval.start:
            i += 1
        intervals.insert(i, newInterval)
        i -= 1
        # for j in intervals:
        #     print [j.start, j.end]
        while i >= 0 and intervals[i].end >= intervals[i + 1].start:
            intervals[i + 1].start = intervals[i].start
            if intervals[i + 1].end < intervals[i].end:
                intervals[i + 1].end = intervals[i].end
            intervals.pop(i)
            i -= 1
        i = i + 2
        while i < len(intervals) and intervals[i].start <= intervals[i - 1].end:
            if intervals[i].end > intervals[i - 1].end:
                intervals[i - 1].end = intervals[i].end
            intervals.pop(i)
        return intervals