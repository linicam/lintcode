# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/permutations-ii
@Language: Python
@Datetime: 17-01-22 00:27
'''

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    res = []
    def permuteUnique(self, nums):
        # write your code here
        if not len(nums):
            return [[]]
        self.permuteCore(nums, 0)
        return self.res
            
    def permuteCore(self, num, start):
        if start == len(num):
            self.res.append(num[:])
        swp = []
        for i in range(start, len(num)):
            if num[i] in swp:
                continue
            swp.append(num[i])
            num[start], num[i] = num[i], num[start]
            self.permuteCore(num, start + 1)
            num[start], num[i] = num[i], num[start]

