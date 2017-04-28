# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/wiggle-sort-ii
@Language: Python
@Datetime: 17-02-18 16:10
'''

class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        # Write your code here
        nums.sort()
        t = (len(nums) + 1) // 2
        a = nums[:t]
        b = nums[t:]
        for i in range(len(b)):
            if i + 1 < len(b) and b[i] == a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                b[i], b[i + 1] = b[i + 1], b[i]
            nums[2*i] = a[i]
            nums[2*i + 1] = b[i]
                
        if len(a) > len(b):
            nums[len(nums) - 1] = a[len(a) - 1]