#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 19:51:20 2017

@author: zhangchi
"""

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        dictionary = {}
        for line in wall:
            temp = 0
            for item in line:
                temp += item
                if temp in dictionary:
                    dictionary[temp] += 1
                else:
                    dictionary[temp] = 1
        total = len(wall)
        result = 10001
        no = sum(wall[0])
        for item in dictionary:
            if total - dictionary[item] < result and item != no:
                result = total - dictionary[item]
        if result == 10001:
            result = len(wall)
        return result
        
s = Solution()
print s.leastBricks([[1],[1],[1]])