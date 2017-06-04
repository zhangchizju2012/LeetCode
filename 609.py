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
        
        
s = Solution()
print s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
