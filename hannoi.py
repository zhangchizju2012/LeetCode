#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 17:30:07 2016

@author: zhangchi
"""

def hannoi(n,a,b,c):
    if n == 1:
        print "Move disk " + str(n) + " from " + a + " to " + c
    else:
        hannoi(n-1,a,c,b)
        print "Move disk " + str(n) + " from " + a + " to " + c
        hannoi(n-1,b,a,c)
        
hannoi(2,'a','b','c')