# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/majority-number
@Language: Python
@Datetime: 17-02-18 00:37
'''

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        # r = {}
        # for i in nums:
        #     if not i in r:
        #         r[i] = 1
        #     else:
        #         r[i] += 1
        #     if r[i] > len(nums) / 2:
        #         return i
        # return 0
        nums.sort()
        return nums[len(nums) // 2]
