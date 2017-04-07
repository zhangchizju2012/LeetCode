#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:59:40 2017

@author: zhangchi
"""

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        dictionary = {}
        for item in strs:
            if item in dictionary:
                dictionary[item] += 1
            else:
                dictionary[item] = 1
        '''
        result = -1
        for item in dictionary:
            if dictionary[item] == 1:
                if len(item) > result:
                    result = len(item)
        # ["aaa","aaa","aa"] should return -1
        '''
        candidates = []
        alarm = []
        for item in dictionary:
            if dictionary[item] > 1:
                alarm.append(item)
            else:
                candidates.append(item)
        result = -1
        label = True
        label_2 = True
        for candidate in candidates:
            if len(candidate) > result:
                # there is no need for us to consider candidates whose length is less than result
                for item in alarm:
                    # check whether candidate is a part of item (in alarm)
                    # first check the length of candidate and item can make it faster (not finished)
                    temp = item
                    for alpha in candidate:
                        if alpha in temp:
                            position = temp.find(alpha)
                            temp = temp[position+1:]
                            # only consider the left string, alpha should in the left string
                        else:
                            # candidate is not a part of this item
                            # check whether candidate is a part of another item
                            label_2 = False
                            break
                    if label_2 == True:
                        # candidate is a part of this item, no need check other item
                        # this candidate won't be consider
                        label = False
                        break
                    else:
                        # check whether candidate is a part of another item
                        # for loop to the next item
                        label_2 = True
                if label == True:
                    result = len(candidate)
                else:
                    label = True
        return result
    
s = Solution()
#print s.findLUSlength(["abcabc","abcabc","aab"])
#print s.findLUSlength(["aabbcc", "aabbcc","aabbccc"])
print s.findLUSlength(["aabbcc", "aabbcc","cb","abc"])