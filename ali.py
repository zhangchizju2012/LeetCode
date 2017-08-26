#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 06:00:06 2017

@author: zhangchi
"""

# 1|12|123|1234|...|12345678910111213|.....
# 问第k个数对应什么

def get(count):
    now = 1
    total = 0
    while total + now < count:
        total += now
        now += 1
    return count - total
      
print get(1)