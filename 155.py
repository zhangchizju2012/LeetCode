#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 01:26:50 2017

@author: zhangchi
"""

#关键是要把每个时刻的最小值都给保存下来，那么就可以用list里套（）的方式

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        minValue = self.getMin()
        if minValue is None or x < minValue:
            minValue = x
        self.stack.append((x,minValue))
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
                      
'''

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
        if self.minValue is None or x < self.minValue:
            self.minValue = x
        self.stack.append((x,self.minValue))
        

    def pop(self):
        """
        :rtype: void
        """
        result = self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

'''
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()