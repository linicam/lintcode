# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/minimum-subarray
@Language: Python
@Datetime: 17-01-25 18:54
'''

class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        mmax = sum = 0
        # start, end = 0, 1
        # ti, tj = 0, 1
        for i in range(len(nums)):
            sum += nums[i]
            if sum <= mmax:
                # start = ti
                # end = tj
                mmax = sum
            elif sum > 0:
                # ti = i + 1
                # tj = i + 2
                sum = 0
            # else:
            #     tj += 1
        if mmax == 0:
            mmax = nums[0]
            for i in nums:
                mmax = min(mmax, i)
        return mmax
