#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 01:26:50 2017

@author: zhangchi
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minValue = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.minValue is None or x < self.minValue:
            self.minValue = x
        

    def pop(self):
        """
        :rtype: void
        """
        result = self.stack.pop()
        if result == self.minValue:
            self.minValue = None
            for i in self.stack:
                if self.minValue is None or i < self.minValue:
                    self.minValue = i
        return result

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minValue


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()