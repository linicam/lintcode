# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/compare-strings
@Language: Python
@Datetime: 16-12-19 05:26
'''

class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        A = list(A)
        B = list(B)
        while len(B) > 0:
            try:
                i = A.index(B[0])
                A.pop(i)
                B.pop(0)
            except:
                return False
        if len(B) > 0:
            return False
        return True