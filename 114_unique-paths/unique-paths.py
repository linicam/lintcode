# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/unique-paths
@Language: Python
@Datetime: 16-12-20 23:50
'''

class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        num = max(m, n)
        ans, temp = 1, 1
        i, j = m + n - 2, 1
        while i >= num:
            ans *= i
            temp *= j
            i -= 1
            j += 1
        return ans / temp