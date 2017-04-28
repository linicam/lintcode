# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/first-position-of-target
@Language: Python
@Datetime: 16-12-19 05:14
'''

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        i = 0
        j = len(nums)
        while i < j:
            mid = (i + j) / 2
            if nums[mid] > target:
                j = mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                while nums[mid - 1] == nums[mid]:
                    mid -= 1
                return mid
        if nums[i] == target:
            return i
        return -1