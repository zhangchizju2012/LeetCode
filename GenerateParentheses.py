#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 11:33:58 2016

@author: zhangchi
"""

def helpler(l, r, item, res):
    if r < l:
        return
    if l == 0 and r == 0:
        res.append(item)
        #return
    if l > 0:
        helpler(l - 1, r, item + '(', res)
        #return
    if r > 0:
        helpler(l, r - 1, item + ')', res)
        #return

def generateParenthesis(n):
    if n == 0:
        return []
    res = []
    helpler(n, n, '', res)
    return res
    
print generateParenthesis(3)
