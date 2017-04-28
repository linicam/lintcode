# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/partition-array
@Language: Python
@Datetime: 17-01-21 13:38
'''

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        nums.sort()
        for i in range(len(nums)):
            if nums[i] >= k:
                return i 
        return len(nums) if len(nums) > 0 else 0
