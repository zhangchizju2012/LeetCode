#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:14:10 2016

@author: zhangchi
"""

class Solution(object):
    def isNormal(self,s):
        if s != '.' and s != '*':
            return True
        else:
            return False
            
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) >= 2:
            if self.isNormal(p[0]):
                if self.isNormal(p[1]) or p[1] == '.':
                    if len(s) >= 1:
                        if s[0] == p[0]:
                            return True and self.isMatch(s[1:],p[1:])
                        else:
                            return False
                    else:
                        return False
                else:
                    #此处有问题
                    temp = None
                    for i in range(len(s)):
                        if s[i] != p[0]:
                            temp = i
                            break
                    if temp is None:
                        for i in range(2,len(p)):
                            if p[i] != p[0]:
                                return False
                        return True
                    return self.isMatch(s[temp:],p[2:])
                    
            elif p[0] == '.':
                if self.isNormal(p[1]) or p[1] == '.':
                    if len(s) >= 1:
                        return True and self.isMatch(s[1:],p[1:])
                    else:
                        return False
                else:
                    if len(p) == 2:
                        return True
                    else:
                        index = None
                        for i in range(2,len(p)):
                            if p[i] == '*':
                                return False
                            elif p[i] == '.':
                                pass
                            else:
                                index = i
                                break
                        if index is None:
                            return True
                        label = False
                        while label is False and s.find(p[index]) >=0:
                            position = s.find(p[index])
                            label = self.isMatch(s[position:],p[index:])
                            s = s[position+1:]
                        return label
            else:
                return False
        elif len(p) == 1:
            if len(s) == 0 or len(s) > 1:
                return False
            else:
                if p[0] == '*':
                    return False
                elif p[0] == '.':
                    return True
                else:
                    if p[0] == s[0]:
                        return True
                    else:
                        return False
        else:
            if len(s) == 0:
                return True
            else:
                return False
                
S = Solution()
s='aaa'
p='ab*a*c*a'
print S.isMatch(s, p)
'''
"aaa"
"ab*a*c*a"
'''
                