#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 20:00:59 2017

@author: zhangchi
"""

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for item in paths:
            temp = item.split(" ")
            if len(temp) > 1:
                for i in xrange(1,len(temp)):
                    positionA = temp[i].find("(")
                    positionB = temp[i].find(")")
                    txt = temp[i][positionA+1:positionB]
                    if txt in dic:
                        dic[txt].append(temp[0]+'/'+temp[i][:positionA])
                    else:
                        dic[txt] = [temp[0]+'/'+temp[i][:positionA]]
        result = []
        for item in dic:
            if len(dic[item]) > 1:
                result.append(dic[item])
        return result
        
s = Solution()
print s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
