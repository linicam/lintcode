# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/topological-sorting
@Language: Python
@Datetime: 16-12-26 10:15
'''

# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """
    def topSort(self, graph):
        # write your code here
        m = {}
        for i in range(len(graph)):
            for j in graph[i].neighbors:
                if not j in m:
                    m[j] = 1
                else:
                    m[j] += 1
        res = []
        for i in graph:
            if not i in m:
                res.append(i)
        r = []
        while len(res):
            a = res.pop(0)
            r.append(a)
            for i in a.neighbors:
                m[i] -= 1
                if not m[i]:
                    res.append(i)
        return r