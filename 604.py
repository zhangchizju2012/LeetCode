#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 19:45:31 2017

@author: zhangchi
"""

class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.itemList = []
        self.countList = []
        previous = ""
        previousAc = ""
        # 数字不一定只占一位
        for i in xrange(len(compressedString)):
            if compressedString[i].isdigit():
                previous += compressedString[i]
            else:
                if len(previous) == 0:
                    previousAc += compressedString[i]
                else:
                    self.countList.append(int(previous))
                    self.itemList.append(previousAc)
                    previousAc = compressedString[i]
                    previous = ""
        if len(previous) > 0:
            self.countList.append(int(previous))
            self.itemList.append(previousAc)
        self.index = 0
        self.length = len(self.itemList)
        # 数字不一定只占一位，下面的方法当成一位来考虑了
#==============================================================================
#         self.itemList = []
#         self.countList = []
#         count = 0
#         for item in compressedString:
#             if count % 2 == 0:
#                 self.itemList.append(item)
#             else:
#                 self.countList.append(int(item))
#             count += 1
#         self.index = 0
#         self.length = len(self.itemList)
#==============================================================================
        

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext() == False:
            return ' '
        else:
            if self.countList[self.index] > 0:
                self.countList[self.index] -= 1
                return self.itemList[self.index]
            else:
                self.index += 1
                self.countList[self.index] -= 1
                return self.itemList[self.index]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.length == 0:
            return False
        elif self.index >= self.length - 1 and self.countList[self.index] == 0:
            return False
        else:
            return True
            
iterator = StringIterator("")
print iterator.next()
print iterator.next()
print iterator.next()
print iterator.next()
print iterator.next()
print iterator.next()
print iterator.next()
print iterator.hasNext()
print iterator.next()
print iterator.hasNext()
print iterator.next()
