#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 19:05:34 2018

@author: zhangchi
"""
# 找肯定比自己富（包括自己）中，比自己（包括自己）安静的
# recursion解
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        