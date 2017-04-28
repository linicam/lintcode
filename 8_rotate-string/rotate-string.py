# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/rotate-string
@Language: Python
@Datetime: 16-12-19 05:07
'''

class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
	    # write you code here
	    if len(s) < 1:
	        return
	    offset = offset % len(s)
	    while offset > 0:
	        t = s.pop(len(s) - 1)
	        s.insert(0, t)
	        offset -= 1