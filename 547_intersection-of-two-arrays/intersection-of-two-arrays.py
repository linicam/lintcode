# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/intersection-of-two-arrays
@Language: Python
@Datetime: 16-12-19 04:31
'''

class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        nums1.sort()
        nums2.sort()
        res = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] == nums2[j]:
                res.append(nums1[i])
                while i < len(nums1) - 1 and nums1[i+1] == nums1[i]:
                    i += 1
                while j < len(nums2) - 1 and nums2[j + 1] == nums2[j]:
                    j += 1
                i += 1
                j += 1
        return res