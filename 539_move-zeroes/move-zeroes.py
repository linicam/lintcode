# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/move-zeroes
@Language: Python
@Datetime: 16-12-19 04:37
'''

class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        # Write your code here
        count = 0
        i = 0
        while i < len(nums) - count:
            if nums[i] == 0:
                count += 1
                t = nums.pop(i)
                nums.append(t)
                i -= 1
            i += 1