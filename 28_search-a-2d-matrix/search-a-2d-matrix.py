# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/search-a-2d-matrix
@Language: Python
@Datetime: 16-12-20 11:04
'''

class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        i = 0
        j = len(matrix)
        while i < j:
            mid = (i + j) / 2
            if matrix[mid][0] < target:
                i = mid + 1
            elif matrix[mid][0] > target:
                j = mid
            else:
                return True
        a = 0
        b = len(matrix[0]) if i == 0 else len(matrix[i - 1])
        while a < b:
            mid = (a + b) / 2
            if matrix[i - 1][mid] < target:
                a = mid + 1
            elif matrix[i - 1][mid] > target:
                b = mid
            else:
                return True
        return False
