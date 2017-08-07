#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 22:28:38 2017

@author: zhangchi
"""

class Solution(object):
    def itemAssociation(self, itemList):
        groupList = []
        label = True
        for a,b in itemList:
            label = False
            for group in groupList:
                if a in group or b in group:
                    label = True
                    group.add(a)
                    group.add(b)
                    break
            if label is False:
                group = set()
                group.add(a)
                group.add(b)
                label = True
        # 然后所有的group都在grouplist里了，然后找最长的，最长的有并列就再按字母顺序，懒的写了