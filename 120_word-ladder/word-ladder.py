# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/word-ladder
@Language: Python
@Datetime: 16-12-27 12:05
'''

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    
    # setålistï¼å¨å xx in yyçæ¶åï¼setè¦æ¯listå¿«
    def ladderLength(self, start, end, dict):
        # write your code here
        r = [[start, 1]]
        dict.add(end)
        le = len(start)
        while r:
            po = r.pop(0)
            p, cc = po[0], po[1]
            if p == end:
                return cc
            for i in xrange(le):
                p1, p2 = p[:i], p[i + 1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if p[i] != j:
                        new = p1 + j + p2
                        if new in dict:
                            r.append([new, cc + 1])
                            dict.remove(new)
        return 0
    
    # 2, right one
    # def ladderLength(self, start, end, dict):
    #     # write your code here
    #     dict.add(end)
    #     wordLen = len(start)
    #     queue = collections.deque([(start, 1)])
    #     while queue:
    #         curr = queue.popleft()
    #         currWord = curr[0]; currLen = curr[1]
    #         if currWord == end: return currLen
    #         for i in xrange(wordLen):
    #             part1 = currWord[:i]; part2 = currWord[i+1:]
    #             for j in 'abcdefghijklmnopqrstuvwxyz':
    #                 if currWord[i] != j:
    #                     nextWord = part1 + j + part2
    #                     if nextWord in dict:
    #                         queue.append((nextWord, currLen + 1))
    #                         dict.remove(nextWord)
    #     return 0
    
    
    # 3, time limit exceeded
    # def ladderLength(self, start, end, dict):
    #     # write your code here
    #     m = {}
    #     m[start] = 1
    #     r = [start]
    #     dict = list(dict)
    #     if not end in dict:
    #         dict.append(end)
    #     le = len(start)
    #     while r:
    #         a = r.pop(0)
    #         i = 0
    #         while i < len(dict):
    #             if self.mcompare(a, dict[i]):
    #                 if dict[i] in m:
    #                     m[dict[i]] = min(m[a] + 1, m[dict[i]])
    #                 else:
    #                     m[dict[i]] = m[a] + 1
    #                 r.append(dict[i])
    #                 dict.pop(i)
    #                 i -= 1
    #             i += 1
    #     return 0
                
    # def mcompare(self, a, b):
    #     count = 0
    #     for i in range(len(a)):
    #         if a[i] != b[i]:
    #             count += 1
    #     return count == 1
        
    # 4, for word ladder ii
    # def getEntry(self, word, index):
    #     return word[:index] + word[index + 1:]
        
    # def buildIndexes(self, length, dict):
    #     indexes = []
    #     for i in range(length):
    #         index = {}
    #         for word in dict:
    #             entry = self.getEntry(word, i)
    #             words = index.get(entry, [])
    #             words.append(word)
    #             index[entry] = words
    #         indexes.append(index)
    #     return indexes

    # def BFS(self, start, end):
    #     self.distance = {}
    #     self.distance[start] = 0
    #     queue = [start]
    #     while len(queue) != 0:
    #         head = queue[0]
    #         del queue[0]
    #         for word in self.getNextWord(head):
    #             if word not in self.distance:
    #                 self.distance[word] = self.distance[head] + 1
    #                 queue.append(word)
                    
    # def getNextWord(self, word):
    #     for i in range(len(word)):
    #         entry = self.getEntry(word, i)
    #         print i, self.indexes[i]
    #         if entry in self.indexes[i]:
    #             for nextWord in self.indexes[i][entry]:
    #                 if nextWord != word:
    #                     yield nextWord
                    
    # def ladderLength(self, start, end, dict):
    #     if start is None or end is None or len(start) != len(end):
    #         return []
    #     self.dict = list(dict)
    #     if not start in self.dict:
    #         self.dict.append(start)
    #     if not end in self.dict:
    #         self.dict.append(end)
    #     self.indexes = self.buildIndexes(len(start), self.dict)
    #     print self.indexes
    #     self.BFS(end, start)
    #     return self.distance[start] + 1
            