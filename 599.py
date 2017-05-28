#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 19:39:21 2017

@author: zhangchi
"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic = {}
        for index, item in enumerate(list1):
            dic[item] = index
        result = []
        value = float('inf')
        for index, item in enumerate(list2):
            if item in dic:
                if index + dic[item] < value:
                    value = index + dic[item]
                    result = [item]
                elif index + dic[item] == value:
                    result.append(item)
        return result
        
s = Solution()
#print s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])
print s.findRestaurant(["Shogun", "KFC","Tapioca Express", "Burger King"],["KFC", "Shogun", "Burger King"])