#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:15:03 2017

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
            return True
        left = 0
        right = len(self.array) - 1
        if right == -1:
            self.array.append([start, end, 1])
            #print self.array
            return True
        while left <= right:
            mid = left + (right-left) // 2
            value = self.array[mid][0]
            if value == start:
                if self.array[mid][2] >= 2:
                    return False
                else:
                    second = self.array[mid][1]
                    if second == end:
                        self.array[mid][2] = 2
                        return True
                    elif second < end:
                        self.array[mid][2] = 2
                        #self.array = self.array[:mid+1] + [[second, end, 1]] + self.array[mid+1:]
                        return self.book(second, end)
                    else:
                        self.array[mid][1] = end
                        self.array[mid][2] = 2
                        self.array = self.array[:mid+1] + [[end, second, 1]] + self.array[mid+1:]
                        return True
            elif value < start:
                left = mid + 1
            else:
                right = mid - 1
        if (left == 0 or self.array[left-1][1] <= start) and (left == len(self.array) or end <= self.array[left][0]):
            self.array = self.array[:left] + [[start, end, 1]] + self.array[left:]
            #print self.array
            return True
        else:
            if left == 0:
                if self.book(self.array[left][0], end):
                    self.array = [[start, self.array[left][0], 1]] + self.array
                    return True
                else:
                    return False
            elif left == len(self.array):
                if self.book(start, self.array[left-1][1]):
                    self.array = self.array + [[self.array[left-1][1], end, 1]]
                    return True
                else:
                    return False
            else:
                self.array = self.array[:left] + [[start, end, 1]] + self.array[left:]
                    