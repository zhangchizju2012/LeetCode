#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 01:33:41 2017

@author: zhangchi
"""

def  krakenCount(m, n):
    result = [[1] * n for _ in range(m)] # the left and up one should all be 1
    for i in range(1,m):
        for j in range(1,n):
            result[i][j] = result[i-1][j] + result[i][j-1] + result[i-1][j-1]
            # position (i,j) can be reached from position (i-1,j), (i,j-1) & (i-1,j-1)
    return result[m-1][n-1]

print krakenCount(2,3)