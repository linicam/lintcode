# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/recover-rotated-sorted-array
@Language: Python
@Datetime: 17-01-25 17:26
'''

class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        # i = 1
        # while nums[i - 1] < nums[i] and i < len(nums):
        #     i += 1
        # nums = nums[i:] + nums[:i]
        # return nums
        nums.sort()
        