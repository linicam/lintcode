# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/anagrams
@Language: Python
@Datetime: 16-12-19 06:55
'''

class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        # t = []
        # t.extend(strs)
        # for i in range(len(strs)):
        #     k = list(strs[i])
        #     k.sort()
        #     strs[i] = ''.join(k)
        # res = []
        # while len(strs):
        #     sum = []
        #     sum.append(t[0])
        #     i = 1
        #     while i < len(strs):
        #         if strs[i] == strs[0]:
        #             sum.append(t[i])
        #             strs.pop(i)
        #             t.pop(i)
        #             i -= 1
        #         i += 1
        #     if len(sum) > 1:
        #         res.extend(sum)
        #     t.pop(0)
        #     strs.pop(0)
        # return res
        t = []
        t.extend(strs)
        for i in range(len(strs)):
            k = list(strs[i])
            k.sort()
            strs[i] = ''.join(k)
        res = []
        d = {}
        for i, ele in enumerate(strs):
            if ele in d:
                d[ele].append(i)
            else:
                d[ele] = [i]
        for k in d.keys():
            if len(d[k]) > 1:
                while len(d[k]):
                    res.append(t[d[k].pop()])
        return res