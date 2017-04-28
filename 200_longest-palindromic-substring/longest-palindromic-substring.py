# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/longest-palindromic-substring
@Language: Python
@Datetime: 17-02-18 15:54
'''

class Solution:
    # @param {string} s input string
    # @return {string} the longest palindromic substring
    res = ""
    maxL = 0
    str = ""
    def longestPalindrome(self, s):
        # Write your code here
        if len(s) == 1:
            return s
        self.str = s
        for i in range(len(s) - 1):
            self.findPS(i, False)
            if s[i] == s[i + 1]:
                self.findPS(i, True)
        return self.res
                
    def findPS(self, ind, isDouble):
        tmp = 2 if isDouble else 1
        if self.maxL < tmp:
            self.res = self.str[ind : ind + tmp]
            self.maxL = tmp
        x = ind - 1
        y = ind + tmp
        while x > -1 and y < len(self.str):
            if self.str[x] != self.str[y]:
                return
            if y - x + 1 > self.maxL:
                self.res = self.str[x : y + 1]
                self.maxL = y - x + 1
            x -= 1
            y += 1