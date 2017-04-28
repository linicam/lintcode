# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/3sum-closest
@Language: Python
@Datetime: 16-12-19 23:35
'''

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        min = abs(numbers[0]+numbers[1]+numbers[2]-target)
        res = numbers[0] + numbers[1] + numbers[2]
        for i in range(len(numbers)):
            j = i + 1
            k = len(numbers) - 1
            while j < k:
                sum = numbers[i] + numbers[j] + numbers[k]
                if abs(sum - target) < min:
                    min = abs(sum - target)
                    res = sum
                if sum > target:
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    return target
        return res
                