# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/next-permutation
@Language: Python
@Datetime: 17-01-21 20:17
'''

class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
        nums = num
        if not nums: return []
        j = len(nums)-1
        while j > 0:
            if nums[j-1] < nums[j]: # first one violates the trend
              j = j - 1
              break
            j-=1
            if not j:
                j = -1
        # print i, j, nums
        for i in xrange(len(nums)-1, -1, -1):
            if nums[i] > nums[j]: # 
                nums[i], nums[j] = nums[j], nums[i] # swap position
                nums[j+1:] = sorted(nums[j+1:]) # sort rest
                return nums
        return nums

        # nums = num
        # if not nums: return []
        # i = len(nums)-1
        # j = -1 # j is set to -1 for case `4321`, so need to reverse all in following step
        # while i > 0:
        #     if nums[i-1] < nums[i]: # first one violates the trend
        #       j = i-1
        #       break
        #     i-=1
        # # print i, j, nums
        # for i in xrange(len(nums)-1, -1, -1):
        #     if nums[i] > nums[j]: # 
        #         nums[i], nums[j] = nums[j], nums[i] # swap position
        #         nums[j+1:] = sorted(nums[j+1:]) # sort rest
        #         return nums
        # return nums
