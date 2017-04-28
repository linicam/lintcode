# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/triangle
@Language: Python
@Datetime: 16-12-27 22:55
'''

class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        if not triangle:
            return 0
        l = len(triangle)
        for i in xrange(l):
            if not i:
                continue
            for j in xrange(i + 1):
                if not j:
                    triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
                elif j == i:
                    triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]
        # print triangle
        return min(triangle[l - 1])