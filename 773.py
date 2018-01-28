#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:21:56 2018

@author: zhangchi
"""

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        if board == [[1,2,3],[4,5,0]]:
            return 0
        target = "".join(["".join([str(s) for s in item]) for item in board])
        dic = set()
        now = 1
        nowList = ["123450"]
        # 从终点往回查（从起点也可以），层次性地bfs，查到了就行了
        while len(nowList) > 0:
            temp = []
            for item in nowList:
                result = self.checkPossiblity(item)
                for item in result:
                    if item not in dic:
                        if item == target:
                            return now
                        else:
                            dic.add(item)
                            temp.append(item)
            now += 1
            nowList = temp
        return -1

    def checkPossiblity(self, s):
        # 所有的可能性
        if s[0] == "0":
            return [s[1]+s[0]+s[2]+s[3]+s[4]+s[5], s[3]+s[1]+s[2]+s[0]+s[4]+s[5]]
        elif s[1] == "0":
            return [s[1]+s[0]+s[2]+s[3]+s[4]+s[5], s[0]+s[4]+s[2]+s[3]+s[1]+s[5], s[0]+s[2]+s[1]+s[3]+s[4]+s[5]]
        elif s[2] == "0":
            return [s[0]+s[2]+s[1]+s[3]+s[4]+s[5], s[0]+s[1]+s[5]+s[3]+s[4]+s[2]]
        elif s[3] == "0":
            return [s[3]+s[1]+s[2]+s[0]+s[4]+s[5], s[0]+s[1]+s[2]+s[4]+s[3]+s[5]]
        elif s[4] == "0":
            return [s[0]+s[1]+s[2]+s[4]+s[3]+s[5], s[0]+s[4]+s[2]+s[3]+s[1]+s[5], s[0]+s[1]+s[2]+s[3]+s[5]+s[4]]
        elif s[5] == "0":
            return [s[0]+s[1]+s[2]+s[3]+s[5]+s[4], s[0]+s[1]+s[5]+s[3]+s[4]+s[2]]
        
s = Solution()
print s.slidingPuzzle([[1,2,3],[4,0,5]])
print s.slidingPuzzle([[1,2,3],[5,4,0]])
print s.slidingPuzzle([[4,1,2],[5,0,3]])
print s.slidingPuzzle([[3,2,4],[1,5,0]])