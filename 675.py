#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 20:25:44 2017

@author: zhangchi
"""

class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        self.forest = {}
        self.row = row = len(forest)
        self.col = col = len(forest[0])
        for i in xrange(self.row):
            for j in xrange(self.col):
                self.forest[(i,j)] = forest[i][j]
        for i in xrange(self.row):
            self.forest[(i,-1)] = 0
            self.forest[(i,self.col)] = 0
        for i in xrange(self.col):
            self.forest[(-1,i)] = 0
            self.forest[(self.row,i)] = 0
        dic = {}
        heigthList = []
        for i in xrange(row):
            for j in xrange(col):
                if forest[i][j] > 1: # 0的不能走，1的不用处理
                    heigthList.append(forest[i][j])
                    dic[forest[i][j]] = (i,j)
        heigthList.sort()
        # 从0，0这个位置开始
        if len(heigthList) == 0 or heigthList[0] != forest[0][0]:
            heigthList = [forest[0][0]] + heigthList
            if forest[0][0] == 0 or 1: # 0或者1的话得补充一下dic
                dic[forest[0][0]] = (0,0)
        result = 0
        for i in xrange(len(heigthList)-1):
            temp = self.measureDistance(dic[heigthList[i]],dic[heigthList[i+1]])
            if temp == -1:
                return -1
            else:
                result += temp
        return result
        
    def measureDistance(self,a,b):
        # 计算两点间的路程，bfs
        count = 1
        visited = set()
        visited.add(a)
        lastVisited = set()
        lastVisited.add(a)
        nextVisited = set()
        while len(lastVisited) > 0:
            for (i,j) in lastVisited:
                if (i-1,j) == b:
                    return count
                if (i-1,j) not in visited and self.forest[(i-1,j)] != 0:
                    nextVisited.add((i-1,j))
                    visited.add((i-1,j))
                if (i+1,j) == b:
                    return count
                if (i+1,j) not in visited and self.forest[(i+1,j)] != 0:
                    nextVisited.add((i+1,j))
                    visited.add((i+1,j))
                if (i,j-1) == b:
                    return count
                if (i,j-1) not in visited and self.forest[(i,j-1)] != 0:
                    nextVisited.add((i,j-1))
                    visited.add((i,j-1))
                if (i,j+1) == b:
                    return count
                if (i,j+1) not in visited and self.forest[(i,j+1)] != 0:
                    nextVisited.add((i,j+1))
                    visited.add((i,j+1))
            count += 1
            lastVisited = set(nextVisited)
            nextVisited = set()
        return -1
a = [
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
#a = [[54581641,64080174,24346381,69107959],[86374198,61363882,68783324,79706116],[668150,92178815,89819108,94701471],[83920491,22724204,46281641,47531096],[89078499,18904913,25462145,60813308]]
s = Solution()
print s.cutOffTree(a)
        
        