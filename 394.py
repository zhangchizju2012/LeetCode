#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:20:55 2017

@author: zhangchi
"""

class Solution(object):
    def decodeString(self, s):
        # 看着test case写，还是挺直接的， by myself
        number = ""
        stack = []
        for item in s:
            if item in '0123456789':
                number += item
            elif item == '[':
                stack.append([int(number),""])
                number = ""
            elif item == ']':
                count, cha = stack.pop()
                if len(stack) > 0:
                    stack[-1][1] += count * cha
                else:
                    stack.append([1, count * cha])
            else:
                if len(stack) > 0:
                    stack[-1][1] += item
                else:
                    stack.append([1, item])
        return stack[-1][1]

    def decodeString3(self, s):
        #https://discuss.leetcode.com/topic/57121/share-my-python-stack-simple-solution-easy-to-understand
        stack = []
        stack.append(["", 1])#no need add line 24, 25, 29, 30 because of this line
        num = ""
        for ch in s:
            if ch.isdigit():
              num += ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
            else:
                stack[-1][0] += ch
        return stack[0][0]
    # wrong
    def decodeString2(self, s):
        """
        :type s: str
        :rtype: str
        """
        number = ""
        numberStack = []
        charaStack = []
        result = ""
        cha = ""
        for item in s:
            if item in '0123456789':
                number += item
                if cha != "":
                    charaStack.append(cha)
                    cha = ""
            elif item == '[':
                numberStack.append(int(number))
                number = ""
            elif item == ']':
                count = numberStack.pop()
                #chara = charaStack.pop()
                if len(charaStack) > 0:
                    if len(numberStack) > 0:
                        temp = charaStack.pop()
                        temp = temp + count * cha
                        charaStack.append(temp)
                    else:
                        cha = charaStack.pop()
                        result += count * cha
                else:
                    result += count * cha
                cha = ""
            else:
                cha += item
        if cha != "":
            result += cha
        return result
        
s = Solution()
print s.decodeString("sd2[f2[e]g]i")