# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/interleaving-string
@Language: Python
@Datetime: 16-12-30 10:22
'''

class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        if not len(s1) + len(s2) == len(s3):
            return False
        m, n = len(s1), len(s2)
        f = [[False] * (m + 1) for i in range(n + 1)]
        flag = True
        f[0][0] = flag
        for i in range(1, m + 1):
            if s1[i - 1] != s3[i - 1]:
                flag = False
            f[0][i] = flag
        flag = True
        for i in range(1, n + 1):
            if s2[i - 1] != s3[i - 1]:
                flag = False
            f[i][0] = flag
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s3[i + j - 1] == s2[i - 1] and not f[i][j]:
                    f[i][j] = f[i - 1][j]
                if s3[i + j - 1] == s1[j - 1] and not f[i][j]:
                    f[i][j] = f[i][j - 1]
        # print f
        return f[n][m]