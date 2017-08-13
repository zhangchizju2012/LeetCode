#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 19:29:13 2017

@author: zhangchi
"""

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dic = {0:0,1:0}
        for item in moves:
            if item == "R":
                dic[0] += 1
            elif item == "L":
                dic[0] -= 1
            elif item == "U":
                dic[1] += 1
            elif item == "D":
                dic[1] -= 1
        if dic[0] == 0 and dic[1] == 0:
            return True
        else:
            return False