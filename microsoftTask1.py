#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:49:23 2017

@author: zhangchi
"""

def convert(date, format0, format1):
    yidx = format0.find('yyyy')
    midx = format0.find('mm')
    didx = format0.find('dd')
    if didx == -1:
        didx = format0.find('mm',midx+1)
    if midx == -1:
        midx = format0.find('dd',didx+1)
    yy = int(date[yidx:yidx+4])
    dd = int(date[didx:didx+2])
    mm = int(date[midx:midx+2])
    yidx = format1.find('yyyy')
    didx = format1.find('dd')
    midx = format1.find('mm')
    ret = format1
    ret = ret.replace('yyyy', str(yy))
    ret = ret.replace('dd', "%02d"%(dd,))
    ret = ret.replace('mm', "%02d"%(mm,))
    return ret

def convertFull():
    File = open("Calendar-confusion_InputForSubmission_2.txt")
    for line in File:
        eachLine = line.strip().split(' ')
        print convert(eachLine[0],eachLine[1],eachLine[2])
        
convertFull()
    
        

        