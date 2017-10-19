#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 19:50:32 2017

@author: zhangchi
"""

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digList = set()
        for index, item in enumerate(time):
            if index != 2:
                digList.add(int(item))
        candidate = []
        for i1 in digList:
            for i2 in digList:
                left = i1 * 10 + i2
                if 0 <= left < 24:
                    for i3 in digList:
                        for i4 in digList:
                            right = i3 * 10 + i4
                            if 0 <= right < 60:4
                                candidate.append(left*100+right)
        candidate.sort()
        origin = int(time[:2]) * 100 + int(time[-2:])
        if candidate[-1] <= origin:
            temp = str(candidate[0])
            temp = (4-len(temp)) * "0" + temp
            return temp[:2] + ":" + temp[-2:]
        else:
            for item in candidate:
                if item > origin:
                    temp = str(item)
                    temp = (4-len(temp)) * "0" + temp
                    return temp[:2] + ":" + temp[-2:]
        #candidate.sort(key=lambda x:x[1])
        #candidate.sort(key=lambda x:x[0])
        
        #return candidate, origin
    
s = Solution()
print s.nextClosestTime("01:32")