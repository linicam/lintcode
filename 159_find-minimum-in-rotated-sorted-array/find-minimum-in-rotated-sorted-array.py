# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array
@Language: Python
@Datetime: 17-01-21 14:33
'''

class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        # write your code here
        if not len(nums) or nums[0] < nums[len(nums) - 1]:
            return nums[0]
        if nums[1] < nums[0]:
            return nums[1]
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (i + j) / 2
            if mid == i:
                break
            if nums[mid] > nums[j]:
                i = mid
            elif nums[mid] < nums[j]:
                j = mid
        return nums[j]
                