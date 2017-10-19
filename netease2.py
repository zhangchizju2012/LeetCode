#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 02:01:07 2017

@author: zhangchi
"""

#coding = utf-8
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = 4
    a = "1 2 3 4"
    line = a.split()
    result = []
    for item in line:
        result.append(item)
        result = result[::-1]
    print " ".join([str(item) for item in result])
    
# =============================================================================
# #coding = utf-8
# import sys
# 
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     line = sys.stdin.readline().strip().split(" ")
#     result = []
#     for item in line:
#         result.append(item)
#         result = result[::-1]
#     print " ".join([str(item) for item in result])
# =============================================================================
