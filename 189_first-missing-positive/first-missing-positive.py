# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/first-missing-positive
@Language: Python
@Datetime: 17-01-21 04:29
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        # res = {}
        # for i in A:
        #     res[i] = True
        # for i in range(1, len(A) + 2):
        #     if not i in res:
        #         return i
        # return 1
        if not len(A):
            return 1
        a = sorted(A)
        i = 0
        while i < len(a) and a[i] < 1:
            i += 1
        j = 1
        count = 1
        while i + j - 1 < len(a) and a[i + j - 1] <= count:
            # if i + j < len(a) and a[i + j - 1] == a[i + j]:
            #     a.pop(i + j)
            #     continue
            # if a[i + j - 1] != j:
            #     break
            if a[i + j - 1] < count:
                count -= 1
            count += 1
            j += 1
        return count
