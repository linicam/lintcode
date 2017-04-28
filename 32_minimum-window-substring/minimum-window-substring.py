# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/minimum-window-substring
@Language: Python
@Datetime: 17-03-04 02:15
'''

class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        # write your code here
        from collections import Counter, defaultdict
        a = Counter(target)
        sum = 0
        for i in a.values():
            sum += i
        tar = -1
        for i in range(len(source)):
            if source[i] in a:
                a[source[i]] -= 1
                if a[source[i]] >= 0:
                    sum -= 1
                if not sum:
                    tar = i
                    break
        if tar < 0:
            return ""
        start = 0
        source = source[:tar + 1]
        for i in range(len(source)):
            if source[i] in a:
                a[source[i]] += 1
                if a[source[i]] > 0:
                    start = i
                    break
        return source[start:]
        