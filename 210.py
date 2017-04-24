#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:21:36 2017

@author: zhangchi
"""

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        dictionary = {}
        reverse = {}
        for i in range(numCourses):
            dictionary[i] = 0
            reverse[i] = []
        for item in prerequisites:
            dictionary[item[0]] += 1
            reverse[item[1]].append(item[0])
        
        label = True
        result = []
        while label:
            label = False
            for item in dictionary:
                if dictionary[item] == 0:
                    dictionary[item] = 'visited'
                    result.append(item)
                    label = True
                    for course in reverse[item]:
                        dictionary[course] -= 1
        if len(result) == numCourses:
            return result
        else:
            return []