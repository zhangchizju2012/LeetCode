#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Created on Sun Nov  5 15:59:55 2017

@author: zhangchi
"""

class Solution(object):
    def __init__(self):
        self.label = True
        
    def preprocess(self,pattern):
        result = ""
        length = len(pattern)
        index = 0
        while index < length:
            if len(result) < 2:
                result += pattern[index]
                index += 1
            else:
                if result[-1] == "*":
                    if pattern[index] == result[-2]:
                        if index + 1 < length and pattern[index+1] == "*":
                            index += 2
                        else:
                            # a*a*a得变成a*a，而不是a*,因为前者代表至少有一个a
                            result += pattern[index]
                            index += 1
                    else:
                        result += pattern[index]
                        index += 1
                else:
                    result += pattern[index]
                    index += 1
        return result
    
    def isMatch(self, text, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if self.label is True:
            # 预处理只要一次
            pattern = self.preprocess(pattern)
            self.label = False
            
        if len(text) == len(pattern) == 0:
            return True
        elif len(text) == 0:
            if len(pattern) >= 2 and pattern[1] == "*":
                return self.isMatch(text,pattern[2:])
            else:
                return False
        elif len(pattern) == 0:
            return False
        # 以上为长度为0的特殊情况
        else:
            if len(pattern) >= 2 and pattern[1] == "*":
                if pattern[0] == ".":
                    # 分别代表取代 >1个，1个，0个
                    return self.isMatch(text[1:], pattern) \
                        or self.isMatch(text[1:], pattern[2:]) \
                        or self.isMatch(text, pattern[2:])
                elif pattern[0] == text[0]:
                    return self.isMatch(text[1:], pattern) \
                        or self.isMatch(text[1:], pattern[2:]) \
                        or self.isMatch(text, pattern[2:])
                else:
                    return self.isMatch(text, pattern[2:])
            else:
                if pattern[0] == ".":
                    return self.isMatch(text[1:], pattern[1:])
                else:
                    if pattern[0] == text[0]:
                        return self.isMatch(text[1:], pattern[1:])
                    else:
                        return False
                    
# no preprocess version
def is_match(text, pattern):
    if len(text) == len(pattern) == 0:
        return True
    elif len(text) == 0:
        if len(pattern) >= 2 and pattern[1] == "*":
            return is_match(text, pattern[2:])
        else:
            return False
    elif len(pattern) == 0:
        return False
    else:
        if len(pattern) >= 2 and pattern[1] == "*":
            if pattern[0] == ".":
                return is_match(text[1:], pattern) \
                    or is_match(text[1:], pattern[2:]) \
                    or is_match(text, pattern[2:])
            elif pattern[0] == text[0]:
                return is_match(text[1:], pattern) \
                    or is_match(text[1:], pattern[2:]) \
                    or is_match(text, pattern[2:])
            else:
                return is_match(text, pattern[2:])
        else:
            if pattern[0] == ".":
                return is_match(text[1:], pattern[1:])
            else:
                if pattern[0] == text[0]:
                    return is_match(text[1:], pattern[1:])
                else:
                    return False
                
# =============================================================================
# "aaa","a*a"
# "abaa", "a.*a*"
# "bbbba", ".*a*a"
# "aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*c" (TLE)
# "a",".*..a*"
# "cbaacacaaccbaabcb","c*b*b*.*ac*.*bc*a*"
# "b","bc*a*"
#print preprocess("c*b*b*.*ac*.*bc*a*")
#print is_match("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*c")
# =============================================================================
s = Solution()
print s.isMatch("cbaacacaaccbaabcb","c*b*b*.*ac*.*bc*a*")

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
                