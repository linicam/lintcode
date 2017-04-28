# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/largest-number
@Language: Python
@Datetime: 17-01-01 12:51
'''

class Solution:	
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        # write your code here
        a = [[] for i in range(10)]
        for i in num:
            t = int(str(i)[0])
            a[t].append(str(i))
            
        for j in a:
            j.sort(self.comp)
        res = ''
        k = 9
        while k >= 0:
            for l in a[k]:
                res += l
            k -= 1
            if not len(res) and k == 0:
                return '0'
        return res
            
    def comp(self, a, b):
        return int(long(b + a) - long(a + b))