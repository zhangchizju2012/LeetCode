#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 19:41:31 2017

@author: zhangchi
"""

class MyCalendar(object):

    def __init__(self):
        self.array = []
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if start >= end:
            return False
        left = 0
        right = len(self.array) - 1
        if right == -1:
            self.array.append([start, end])
            #print self.array
            return True
        while left <= right:
            mid = left + (right-left) // 2
            value = self.array[mid][0]
            if value == start:
                return False
            elif value < start:
                left = mid + 1
            else:
                right = mid - 1
        if (left == 0 or self.array[left-1][1] <= start) and (left == len(self.array) or end <= self.array[left][0]):
            self.array = self.array[:left] + [[start, end]] + self.array[left:]
            #print self.array
            return True
        else:
            return False
    
s = MyCalendar()
print s.book(10,20)
print s.book(15,25)
print s.book(20,30)
