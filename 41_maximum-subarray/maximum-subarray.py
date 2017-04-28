# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/maximum-subarray
@Language: Python
@Datetime: 16-12-28 10:42
'''

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        mmax = sum = 0
        # start, end = 0, 1
        # ti, tj = 0, 1
        for i in range(len(nums)):
            sum += nums[i]
            if sum >= mmax:
                # start = ti
                # end = tj
                mmax = sum
            elif sum < 0:
                # ti = i + 1
                # tj = i + 2
                sum = 0
            # else:
            #     tj += 1
        if mmax == 0:
            mmax = nums[0]
            for i in nums:
                mmax = max(mmax, i)
        return mmax
                
                
            