#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 20:21:07 2017

@author: zhangchi
"""

class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 1
        lights = [True] * n
        result = set()
        if m > 4: # 大于4的没用，都是重复的
            if m % 2 == 1:
                m = 3
            else:
                m = 4
        if m == 1 or m == 3:
            # 现在是穷举，hardcode不太好
            result.add(tuple(self.c1(lights)))
            result.add(tuple(self.c2(lights)))
            result.add(tuple(self.c3(lights)))
            result.add(tuple(self.c4(lights)))
            if m == 3:
                result.add(tuple(self.c1(self.c2(self.c3(lights)))))
                result.add(tuple(self.c1(self.c2(self.c4(lights)))))
                result.add(tuple(self.c1(self.c3(self.c4(lights)))))
                result.add(tuple(self.c2(self.c3(self.c4(lights)))))
        elif m == 2 or m == 4:
            result.add(tuple(lights))
            result.add(tuple(self.c1(self.c2(lights))))
            result.add(tuple(self.c1(self.c3(lights))))
            result.add(tuple(self.c1(self.c4(lights))))
            result.add(tuple(self.c2(self.c3(lights))))
            result.add(tuple(self.c2(self.c4(lights))))
            result.add(tuple(self.c3(self.c4(lights))))
            if m == 4:
                result.add(tuple(self.c1(self.c2(self.c3(self.c4(lights))))))
        return len(result)
            
    def c1(self, temp):
        lights = list(temp)
        for index in xrange(len(lights)):
            lights[index] = not lights[index]
        return lights
    
    def c2(self, temp):
        lights = list(temp)
        for index in xrange(len(lights)):
            if (index+1) % 2 == 1:
                lights[index] = not lights[index]
        return lights
    
    def c3(self, temp):
        lights = list(temp)
        for index in xrange(len(lights)):
            if (index+1) % 2 == 0:
                lights[index] = not lights[index]
        return lights
    
    def c4(self, temp):
        lights = list(temp)
        for index in xrange(len(lights)):
            if (index+1) % 3 == 1:
                lights[index] = not lights[index]
        return lights
    
s = Solution()
print s.flipLights(3,1)