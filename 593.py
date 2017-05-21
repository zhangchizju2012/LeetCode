#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 19:42:12 2017

@author: zhangchi
"""

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4:
            return False
        cord = [p1,p2,p3,p4]
        cord.sort(key=lambda x:x[1])
        cord.sort(key=lambda x:x[0])
        if cord[0][0] - cord[1][0] == cord[2][0] - cord[3][0] \ # x轴差值相等
            and cord[0][1] - cord[1][1] == cord[2][1] - cord[3][1] \ # y轴差值相等
            and (cord[0][0] - cord[1][0]) ** 2 + (cord[0][1] - cord[1][1]) ** 2 == (cord[0][0] - cord[2][0]) ** 2 + (cord[0][1] - cord[2][1]) ** 2 \ # 边长相等，至少是菱形
            and (cord[0][0] - cord[1][0]) ** 2 + (cord[0][1] - cord[1][1]) ** 2 + (cord[0][0] - cord[2][0]) ** 2 + (cord[0][1] - cord[2][1]) ** 2 == (cord[1][0] - cord[2][0]) ** 2 + (cord[1][1] - cord[2][1]) ** 2:
            # 保证是90度角
            return True
        else:
            return False
            
s = Solution()
print s.validSquare([0,0],[1,1],[1,0],[0,1])
#print s.validSquare([1,1],[2,1],[1,1],[2,1])