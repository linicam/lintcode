# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/first-bad-version
@Language: Python
@Datetime: 16-12-20 12:34
'''

#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        if SVNRepo.isBadVersion(1):
            return 1
        if not SVNRepo.isBadVersion(n):
            return -1
        i = 1
        j = n
        while i < j - 1:
            mid = (i + j) / 2
            if SVNRepo.isBadVersion(mid):
                j = mid
            else:
                i = mid
        return j