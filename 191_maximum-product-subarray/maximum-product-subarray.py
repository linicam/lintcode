# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/maximum-product-subarray
@Language: Python
@Datetime: 16-12-28 11:39
'''

class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # write your code here
        if len(nums) == 1 and nums[0] < 1:
            return nums[0]
        num = []
        while 0 in nums:
            t = nums.index(0)
            num.append(nums[:t])
            nums = nums[t + 1:]
        num.append(nums)
        # print num
        pros = []
        for i in range(len(num)):
            nums = num[i]
            first = -1
            last = -1
            count =0
            pro = 1
            for i in range(len(nums)):
                pro *= nums[i]
                if nums[i] < 0:
                    count += 1
                    if first < 0:
                        first = i
                    if last < i:
                        last = i
            if count % 2:
                p1 = p2 = 1
                for i in nums[:last]:
                    p1 *= i
                for i in nums[first + 1:]:
                    p2 *= i
                pro = max(p1, p2)
            pros.append(pro)
        return max(pros)