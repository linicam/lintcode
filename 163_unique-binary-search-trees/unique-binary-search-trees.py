# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/unique-binary-search-trees
@Language: Python
@Datetime: 16-12-21 02:12
'''

class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        # write your code here
        t = [1,1,2]
        i = 3
        while i <= n:
            j = 1
            sum = 0
            while j <= i:
                sum += t[j - 1] * t[i - j]
                j += 1
            t.append(sum)
            i += 1
        return t[n]
        