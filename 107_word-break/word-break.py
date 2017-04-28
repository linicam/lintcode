# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/word-break
@Language: Python
@Datetime: 16-12-30 09:10
'''

class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # write your code here
        # m = {}
        # for i in dict:
        #     m.setDefault(i, True)
        # while s:
        if not len(dict):
            return not s
        m, n = len(s), max([len(t) for t in dict])
        f = [False] * (m + 1)
        f[0] = True
        for i in range(1, m + 1):
            for j in range(1, min(i, n) + 1):
                if not f[i - j]:
                    continue
                if s[i - j:i] in dict:
                    f[i] = f[i - j]
                    break
        return f[m]