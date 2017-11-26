#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 19:59:34 2017

@author: zhangchi
"""

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for item in asteroids:
            if len(stack) == 0 or stack[-1] < 0:
                stack.append(item)
            else:
                if stack[-1] * item > 0:
                    stack.append(item)
                else:
                    label = False
                    while len(stack) > 0 and stack[-1] * item < 0:
                        compare = stack.pop()
                        if abs(compare) == abs(item):
                            label = True
                            break
                        elif abs(compare) > abs(item):
                            label = True
                            stack.append(compare)
                            break
                    if label is False:
                        stack.append(item)
        return stack
    
s = Solution()
print s.asteroidCollision([-2,-2,-2,1])
                            