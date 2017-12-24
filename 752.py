#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 20:03:25 2017

@author: zhangchi
"""

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if "0000" in deadends:
            return -1
        self.result = [[[[float('inf') for _ in xrange(10)] for _ in xrange(10)] for _ in xrange(10)] for _ in xrange(10)]
        self.dic = set()
        for item in deadends:
            self.dic.add((int(item[0]),int(item[1]),int(item[2]),int(item[3])))
            #result[int(item[0])][int(item[1])][int(item[2])][int(item[3])] = float('inf')
        self.result[0][0][0][0] = 0
        for i in range(10) + range(8,-1,-1):
            for j in range(10) + range(8,-1,-1):
                for m in range(10) + range(8,-1,-1):
                    for n in range(10) + range(8,-1,-1):
                        if (i,j,m,n) not in self.dic:
                            self.result[i][j][m][n] = min(min(
                                    self.result[(i+1)%10][j][m][n],
                                    self.result[(i-1)%10][j][m][n],
                                    self.result[i][(j+1)%10][m][n],
                                    self.result[i][(j-1)%10][m][n],
                                    self.result[i][j][(m+1)%10][n],
                                    self.result[i][j][(m-1)%10][n],
                                    self.result[i][j][m][(n+1)%10],
                                    self.result[i][j][m][(n-1)%10],
                                    ) + 1, self.result[i][j][m][n])
        value = self.result[int(target[0])][int(target[1])][int(target[2])][int(target[3])]
        if value == float('inf'):
            return -1
        else:
            return value

# =============================================================================
# class Solution(object):
#     def openLock(self, deadends, target):
#         """
#         :type deadends: List[str]
#         :type target: str
#         :rtype: int
#         """
#         self.result = [[float('inf') for _ in xrange(10)] for _ in xrange(10)]
#         self.dic = set()
#         for item in deadends:
#             self.dic.add((int(item[0]),int(item[1])))
#             #result[int(item[0])][int(item[1])][int(item[2])][int(item[3])] = float('inf')
#         self.helper(0,0,0)
#         #print self.result
#         return self.result[int(target[0])][int(target[1])]
#           
#     def helper(self, i, j, step):
#         if (i,j) not in self.dic:
#             if self.result[i][j] > step:
#                 self.result[i][j] = step
#                 self.helper((i+1)%10,j,step+1)
#                 self.helper((i-1)%10,j,step+1)
#                 self.helper(i,(j+1)%10,step+1)
#                 self.helper(i,(j-1)%10,step+1)
# =============================================================================

# =============================================================================
# class Solution(object):
#     def openLock(self, deadends, target):
#         """
#         :type deadends: List[str]
#         :type target: str
#         :rtype: int
#         """
#         self.result = [[[[float('inf') for _ in xrange(10)] for _ in xrange(10)] for _ in xrange(10)] for _ in xrange(10)]
#         self.dic = set()
#         for item in deadends:
#             self.dic.add((int(item[0]),int(item[1]),int(item[2]),int(item[3])))
#             #result[int(item[0])][int(item[1])][int(item[2])][int(item[3])] = float('inf')
#         self.helper(0,0,0,0,0)
#         return self.result[int(target[0])][int(target[1])][int(target[2])][int(target[3])]
#           
#     def helper(self, i, j, m, n, step):
#         if (i,j,m,n) not in self.dic:
#             if self.result[i][j][m][n] > step:
#                 self.result[i][j][m][n] = step
#                 self.helper((i+1)%10,j,m,n,step+1)
#                 self.helper((i-1)%10,j,m,n,step+1)
#                 self.helper(i,(j+1)%10,m,n,step+1)
#                 self.helper(i,(j-1)%10,m,n,step+1)
#                 self.helper(i,j,(m+1)%10,n,step+1)
#                 self.helper(i,j,(m-1)%10,n,step+1)
#                 self.helper(i,j,m,(n+1)%10,step+1)
#                 self.helper(i,j,m,(n-1)%10,step+1)
# =============================================================================
        
s = Solution()
print s.openLock(["0033","3201","0321","0122","3032","2120","1230","2303","2111","2030"],"0123")
            