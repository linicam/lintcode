# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/median
@Language: Python
@Datetime: 17-02-18 00:28
'''

class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        # write your code here
        nums.sort();
        return nums[(len(nums) - 1) // 2]