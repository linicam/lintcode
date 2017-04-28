# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/distinct-subsequences
@Language: Python
@Datetime: 16-12-29 22:28
'''

class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # write your code here
        # write your code here
    #     dp = [[0 for j in range(len(T) + 1)] for i in range(len(S) + 1)]
    #     for i in range(len(S) + 1):
   	# 		dp[i][0] = 1
    #     for i in xrange(len(S)):
    #         for j in xrange(len(T)):
    #             if S[i] == T[j]:
    #                 dp[i+1][j+1] = dp[i][j+1] + dp[i][j]
    #             else:
    #                 dp[i+1][j+1] = dp[i][j + 1]
    #     return dp[len(S)][len(T)]
        
        
        # n, m = len(S), len(T)
        # f = [[0] * (n + 1) for i in range(m + 1)]
        # for i in range(n + 1):
        #     f[0][i] = 1
        # for i in range(1, m +1):
        #     for j in range(1, n + 1):
        #         if T[i - 1] == S[j - 1]:
        #             f[i][j] = f[i][j - 1] + f[i - 1][j - 1]
        #         else:
        #             f[i][j] = f[i][j - 1]
        # return f[m][n]
        
        
        m, n = len(S), len(T)
        f = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(m + 1):
            f[0][i] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if S[j - 1] == T[i - 1]:
                    f[i][j] = f[i][j - 1] + f[i - 1][j - 1]
                else:
                    f[i][j] = f[i][j - 1]
        return f[n][m]
        
        
        # len1 = len(S)
        # len2 = len(T)
        # f = [[0] * (len2 + 1) for i in range(len1 + 1)] 
        # for i in range(len1 + 1):
        #     f[i][0] = i
        # for j in range(len2 + 1):
        #     f[0][j] = j

        # for i in range(1, len1 + 1):
        #     for j in range(1, len2 + 1):
        #         if word2[j - 1] == word1[i - 1]:
        #             f[i][j] = f[i - 1][j - 1]
        #         else:
        #             f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1

        # return f[len1][len2]
                    
                