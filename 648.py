#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:54:06 2017

@author: zhangchi
"""

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dict2 = {}
        for item in dict:
            if len(item) == 1:
                dict2[item] = True
            else:
                if item[:2] not in dict2:
                    dict2[item[:2]] = set([item])
                else:
                    dict2[item[:2]].add(item)
        result = []
        inputSen = sentence.split(" ")
        for item in inputSen:
            if item[0] in dict2 or len(item) == 1:
                result.append(item[0])
            else:
                if item[:2] not in dict2:
                    result.append(item)
                else:
                    candidate = ""
                    l = float('inf')
                    for thing in dict2[item[:2]]:
                        if len(thing) < l and thing == item[:len(thing)]:
                            candidate = thing
                            l = len(thing)
                    if candidate == "":
                        result.append(item)
                    else:
                        result.append(candidate)
        return " ".join(result)
            
s = Solution()
print s.replaceWords(["cat", "bat", "rat"],"the cattle was rattled by the battery")
                        
                