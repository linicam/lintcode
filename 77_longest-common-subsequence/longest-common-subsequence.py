# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/longest-common-subsequence
@Language: Python
@Datetime: 16-12-29 21:06
'''

class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        n, m = len(A), len(B)
        f = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, n +1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])
        # print f
        return f[n][m]
        
        # # longest common substring
        # res = [[0] * (len(B) + 1) for row in range(len(A) + 1)]
        # cs = 0
        # for i in range(1, len(A) + 1):
        #     for j in range(1, len(B) + 1):
        #         if B[j - 1] == A[i - 1]:
        #             res[i][j] = res[i-1][j-1] + 1
        #         else:
        #             res[i][j] = 0
        #         cs = max(cs, res[i][j])
        # return cs
                
