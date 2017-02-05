#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:44:48 2016

@author: zhangchi
"""

class Solution(object):
    def helpBuildPath(self,m,n):
        if self.dictionary[m-1][n-1] != -1:
            return self.dictionary[m-1][n-1]
        else:
            if m == 1:#上面到顶的情况
                if self.map[m-1][n-2] == 1:#此处不用加n==1的情况，因为m=1,n=1时dictionary[0][0]已知，在前方就已经return值
                    value = 0
                else:
                    value = self.helpBuildPath(m,n-1)
            elif self.map[m-2][n-1] == 1:#上方有障碍物就跟m==1的情况一样，之后的情况探讨也一样（除了多了n=1,n=1相当于前方有障碍物），self.map[m-1][n-2] == 1为了确保前方没有障碍物
                if n == 1 or self.map[m-1][n-2] == 1:
                    value = 0
                else:
                    value = self.helpBuildPath(m,n-1)
                    
            elif n == 1:#左边到顶的情况
                if self.map[m-2][n-1] == 1:
                    value = 0
                else:
                    value = self.helpBuildPath(m-1,n)
            elif self.map[m-1][n-2] == 1:
                if m == 1 or self.map[m-2][n-1] == 1:
                    value = 0
                else:
                    value = self.helpBuildPath(m-1,n)
            else:
                value = self.helpBuildPath(m,n-1) + self.helpBuildPath(m-1,n)
            self.dictionary[m-1][n-1] = value
            return value
            
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        self.map = obstacleGrid
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if self.map[m-1][n-1] == 1 or self.map[0][0] == 1:#起点或者终点有障碍物的情况
            return 0
        self.dictionary = [[-1]*n for _ in range(m)]  #[[0]*n]*m会有问题
        self.dictionary[0][0] = 1
        return self.helpBuildPath(m,n)
        
S = Solution()
#obstacleGrid = [[0],[1],[0]]
#obstacleGrid = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],[0,0],[1,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0]]
#obstacleGrid = [[0, 0, 0,0,0], [0, 1, 0,0,0], [0, 0, 1,1,0],[0, 0, 0,0,0],[0, 0, 0,0,0],[0, 1, 0,0,0]]
obstacleGrid = [[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
print S.uniquePathsWithObstacles(obstacleGrid)