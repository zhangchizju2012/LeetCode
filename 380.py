#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 18:26:58 2017

@author: zhangchi
"""
import random

# https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/
# 答案这种更好，直接用list储存全部数，dic存储每个数对应的index，remove的时候把该remove的数取代为最后一个数

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()
        self.list = []
        self.label = True
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.set:
            self.set.add(val)
            self.list.append(val)
            return True
        else:
            return False
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            self.set.remove(val)
            self.label = False
            return True
        else:
            return False
        
    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.label is False:
            self.list = list(self.set) # 其实并不是完全的O(1),只能保证在没有频繁remove.getRandom切换的情况下倾向于O(1)
        return self.list[random.randint(0,len(self.set)-1)]