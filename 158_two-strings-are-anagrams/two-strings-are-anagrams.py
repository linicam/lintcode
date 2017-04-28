# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/two-strings-are-anagrams
@Language: Python
@Datetime: 17-01-16 22:22
'''

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        # s = list(s)
        # t = list(t)
        # while len(s) > 0:
        #     try:
        #         i = t.index(s[0])
        #         t.pop(i)
        #         s.pop(0)
        #     except:
        #         return False
        # if len(t) > 0:
        #     return False
        # return True
        import collections
        b = collections.defaultdict(int)
        for i in s:
            b[i] += 1
        for j in t:
            if not j in b:
                return False
            b[j] -= 1
            if b[j] < 0:
                return False
        return True