# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/permutations
@Language: Python
@Datetime: 16-12-26 15:48
'''

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    res = []
            
    def permuteCore(self, num, start):
        if start == len(num):
            self.res.append(num[:])
        for i in range(start, len(num)):
            num[start], num[i] = num[i], num[start]
            self.permuteCore(num, start + 1)
            num[start], num[i] = num[i], num[start]
            
            
    def permute(self, nums):
        # write your code here
        if not len(nums):
            return [[]]
        self.permuteCore(nums, 0)
        return self.res
