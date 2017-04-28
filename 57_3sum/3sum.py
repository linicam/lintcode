# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/3sum
@Language: Python
@Datetime: 16-12-20 00:12
'''

class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        res = []
        i = 0
        while i < len(numbers) - 2:
            while i > 0 and i < len(numbers) - 2 and numbers[i] == numbers[i - 1]:
                i += 1
            j = i + 1
            k = len(numbers) - 1
            while j < k:
                sum = numbers[i] + numbers[j] + numbers[k]
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    res.append([numbers[i], numbers[j], numbers[k]])
                    while k > 0 and numbers[k - 1] == numbers[k]:
                        k -= 1
                    while j < len(numbers) - 1 and numbers[j + 1] == numbers[j]:
                        j += 1
                    k -= 1
                    j += 1
            i += 1
        return res