# coding:utf-8
'''
@Copyright:LintCode
@Author:   linicam
@Problem:  http://www.lintcode.com/problem/unique-paths-ii
@Language: Python
@Datetime: 16-12-28 10:05
'''

class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        grid = obstacleGrid
        r = len(grid)
        c = len(grid[0])
        if not r or not c:
            return 0
        val = 1
        for i in range(c):
            if grid[0][i] == 1:
                val = 0
            grid[0][i] = val
        val = 1 if grid[0][0] else 0
        for i in range(1, r):
            if grid[i][0] == 1:
                val = 0
            grid[i][0] = val
        for i in range(1, r):
            for j in range(1, c):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    continue
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[r - 1][c - 1]