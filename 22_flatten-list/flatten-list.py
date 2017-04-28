# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/flatten-list
@Language: Python
@Datetime: 17-01-25 16:42
'''

class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    ans = []
    def flatten(self, nestedList):
        # Write your code here
        if type(nestedList) != list:
            nestedList = [nestedList]
        return self.f(nestedList)
        
    def f(self, array):
        ans = []
        for i in array:
            if type(i) == list:
                ans.extend(self.f(i))
            else:
                ans.append(i)
        return ans
        