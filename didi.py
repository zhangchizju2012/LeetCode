#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 01:59:24 2017

@author: zhangchi
"""
# 无序数组求最大子序列
#coding = utf-8
import sys

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    values = map(int, line.split())
    result = [-float('inf')]
    for item in values:
        if result[-1] < 0:
            result.append(item)
        else:
            result.append(item+result[-1])
    print max(result)

# 无序数组求第K大数
#coding = utf-8
import sys

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    values = map(int, line.split())
    values.sort(reverse=True)
    print values[n-1]