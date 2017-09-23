#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 21:55:17 2017

@author: zhangchi
"""

def hackingTime(cipher, origin):
    result = []
    for a,b in zip(cipher, origin):
        if a.isalpha():
            temp = ord(a)-ord(b)
            if temp < 0:
                temp += 26
            result.append(temp)
    return result

c = "Atvt hrqgse, Cnikg"
o = "Your friend, Alice"
print hackingTime(c,o)