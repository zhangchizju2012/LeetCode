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
    