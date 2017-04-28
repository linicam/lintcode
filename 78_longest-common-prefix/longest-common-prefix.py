# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/longest-common-prefix
@Language: Python
@Datetime: 16-12-19 05:37
'''

class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        if not len(strs):
            return ""
        res = []
        t = 0;
        while t < len(strs[0]):
            p = strs[0][t]
            flag = True
            for j in strs:
                if not len(j) or j[t] != p:
                    flag = False
                    break
            if not flag:
                res = strs[0][:t]
                return res
            t += 1
        return strs[0]