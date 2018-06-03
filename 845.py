#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 18:36:27 2018

@author: zhangchi
"""

class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        flag = False
        up = True
        count = 0
        last = -float('inf')
        result = 0
        for item in A:
            if up is True:
                if item > last:
                    count += 1
                    last = item
                elif item == last:
                    flag = False
                    count = 1
                    last = item
                else:
                    if count > 1:
                        flag = True
                        up = False
                        count += 1
                        last = item
                        if count >= 3:
                            result = max(result, count)
                    else:
                        last = item
            else:
                if item > last:
                    if count >= 3:
                        result = max(result, count)
                    count = 2
                    up = True
                    last = item
                elif item == last:
                    flag = False
                    count = 1
                    last = item
                    up = True
                else:
                    count += 1
                    last = item
                    if count >= 3:
                        result = max(result, count)
        if up is False and flag is True:
            if count >= 3:
                result = max(result, count)
        return result
    
s = Solution()
print s.longestMountain([0,1,0,0,1,1,1,1,1])
# [9,8,7,6,5,4,3,2,1,0]
# [2,3,3,2,0,2]
# [0,0,1,0,0,1,1,1,1,1]