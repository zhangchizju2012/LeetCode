#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:06:05 2017

@author: zhangchi
"""

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        #self.stack = [x] + self.stack
        temp = []
        while len(self.stack) > 0:
            temp.append(self.stack.pop())
        self.stack.append(x)
        while len(temp) > 0:
            self.stack.append(temp.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0


#==============================================================================
# class Queue(object):
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.inStack, self.outStack = [], []
# 
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: nothing
#         """
#         self.inStack.append(x)
# 
#     def pop(self):
#         """
#         :rtype: nothing
#         """
#         self.move()
#         self.outStack.pop()
# 
#     def peek(self):
#         """
#         :rtype: int
#         """
#         self.move()
#         return self.outStack[-1]
# 
#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return (not self.inStack) and (not self.outStack) 
#         
#     def move(self):
#         """
#         :rtype nothing
#         """
#         if not self.outStack:
#             while self.inStack:
#                 self.outStack.append(self.inStack.pop())
#==============================================================================

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()