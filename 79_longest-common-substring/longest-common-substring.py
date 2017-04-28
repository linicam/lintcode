# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/longest-common-substring
@Language: Python
@Datetime: 16-12-29 14:16
'''

class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        res = [[0] * (len(B) + 1) for row in range(len(A) + 1)]
        cs = 0
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if B[j - 1] == A[i - 1]:
                    res[i][j] = res[i-1][j-1] + 1
                else:
                    res[i][j] = 0
                cs = max(cs, res[i][j])
        return cs
                
        
                        
                