#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 14:54:24 2017

@author: zhangchi
"""

class Vector2D(object):
    # 注意[], [[],[]]这些
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.input = vec2d
        self.length = []
        for item in vec2d:
            self.length.append(len(item))
        self.max = len(self.length)
        self.index = 0
        self.now = 0
        self.label = True
        if len(self.length) == 0:
            self.label = False
        else:
            while self.now == self.length[self.index]: #可能开始长度是0的
                self.index += 1
                self.now = 0
                if self.index == len(self.length):
                    self.label = False
                    break
        

    def next(self):
        """
        :rtype: int
        """
        value = self.input[self.index][self.now]
        self.now += 1
        while self.now == self.length[self.index]:
            self.index += 1
            self.now = 0
            if self.index == len(self.length):
                self.label = False
                break
        return value
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.label