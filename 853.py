#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 18:39:22 2018

@author: zhangchi
"""

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if len(position) == 0:
            return 0
        carList = []
        for a,b in zip(position, speed):
            carList.append([target-a, b])
        carList.sort(key=lambda x:x[0])
        print(carList)
        count = 1
        lastTime = float(carList[0][0]) / float(carList[0][1])
        for item in carList:
            time =  float(item[0]) / float(item[1])
            if time <= lastTime:
                pass
            else:
                count += 1
                lastTime = time
        return count
    
s = Solution()
print s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])