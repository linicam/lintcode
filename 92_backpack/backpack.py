# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/backpack
@Language: Python
@Datetime: 16-12-30 14:57
'''

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [0 for x in range(m+1)]
        dp[0] = 1
        ans = 0
        for item in A:
            for i in range(m,-1,-1):
                if i-item >=0 and dp[i-item] > 0:
                    ans = max(ans,i)
                    dp[i] = 1
        return ans    
        # n = len(A)
        # A.sort()
        # f = [0] * (m + 1)
        # for i in A:
        #     for j in range(m, -1, -1):
        #         if j - i > 0 and f[j - i] > 0
                
        
        
        n = len(A)
        f = [0] * (m + 1)
        f[0] = 1
        ans = 0
        for i in A:
            for j in range(m, -1, -1):
                if j - i >= 0 and f[j - i] > 0:
                    ans = max(ans, j)
                    f[i] = 1
        return ans   
                