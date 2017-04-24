#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:52:53 2017

@author: zhangchi
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
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
        while label:
            label = False
            for item in dictionary:
                if dictionary[item] == 0:
                    dictionary[item] = 'visited'
                    label = True
                    for course in reverse[item]:
                        dictionary[course] -= 1
        result = True
        for item in dictionary:
            if dictionary[item] != 'visited':
                result = False
        return result
        
s = Solution()
print s.canFinish(4,[[2,1],[3,2],[2,0]])