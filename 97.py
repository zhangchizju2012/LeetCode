#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 15:40:00 2017

@author: zhangchi
"""

class Solution(object):
    # 总体思路：我自己做的，我自己优化的，submit了很多次
    # s1,s2,s3各自有一个指针，如果s1(s2)的指针指向的数字跟s3指针指向的数字相等，就挪到下一个数
    # 如果s1,s2,s3指向的数都相等，先看看尾部的情况（这个trick只是为了减少recursion的次数）
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        length1 = len(s1)
        length2 = len(s2)
        lenght3 = len(s3)
        if length1 + length2 != lenght3:
            return False
        return self.helper(s1,s2,s3)
                
    def helper(self,s1,s2,s3):
        length1 = len(s1)
        length2 = len(s2)
        lenght3 = len(s3)
        p1 = 0
        p2 = 0
        p3 = 0
        while p3 < lenght3:
            if p1 < length1 and p2 < length2:
                if s1[p1]!=s3[p3] and s2[p2]!=s3[p3]:
                    return False
                elif s1[p1]==s3[p3] and s2[p2]!=s3[p3]:
                    p1 += 1
                    p3 += 1
                elif s1[p1]!=s3[p3] and s2[p2]==s3[p3]:
                    p2 += 1
                    p3 += 1
                else:#要是s1的头和s2的头是相等的，那就翻过来看
                    if s1[-1] != s2[-1]: # 如果翻过来还是相等的，那就别翻了，翻来翻去也花时间
                    # 如果真的要翻过来，先把之前比较过的东西去掉，然后重置length1,2,3;p1,2,3
                        s1 = s1[p1:][::-1]
                        s2 = s2[p2:][::-1]
                        s3 = s3[p3:][::-1]
                        length1 = len(s1)
                        length2 = len(s2)
                        lenght3 = len(s3)
                        p1 = 0
                        p2 = 0
                        p3 = 0
                        if s1[p1]!=s3[p3] and s2[p2]!=s3[p3]:
                            return False
                        elif s1[p1]==s3[p3] and s2[p2]!=s3[p3]:
                            p1 += 1
                            p3 += 1
                        elif s1[p1]!=s3[p3] and s2[p2]==s3[p3]:
                            p2 += 1
                            p3 += 1
                    else:
                        return self.helper(s1[p1+1:],s2[p2:],s3[p3+1:]) or self.helper(s1[p1:],s2[p2+1:],s3[p3+1:])
            elif p1 < length1 and p2 >= length2: #p1或者p2可能有一个到尽头了（其实可以直接比较另一个剩下的和s3剩下的部分，我这里这样还是复杂了）
                if s1[p1]!=s3[p3]:
                    return False
                else:
                    p1 += 1
                    p3 += 1
            else:
                if s2[p2]!=s3[p3]:
                    return False
                else:
                    p2 += 1
                    p3 += 1
        return True
#==============================================================================
#     def isInterleave(self, s1, s2, s3):
#         """
#         :type s1: str
#         :type s2: str
#         :type s3: str
#         :rtype: bool
#         """
#         length1 = len(s1)
#         length2 = len(s2)
#         lenght3 = len(s3)
#         if length1 + length2 != lenght3:
#             return False
#         return self.helper(s1,s2,s3)
#                 
#     def helper(self,s1,s2,s3):
#         length1 = len(s1)
#         length2 = len(s2)
#         lenght3 = len(s3)
#         p1 = 0
#         p2 = 0
#         p3 = 0
#         while p3 < lenght3:
#             if p1 < length1 and p2 < length2:
#                 if s1[p1]!=s3[p3] and s2[p2]!=s3[p3]:
#                     return False
#                 elif s1[p1]==s3[p3] and s2[p2]!=s3[p3]:
#                     p1 += 1
#                     p3 += 1
#                 elif s1[p1]!=s3[p3] and s2[p2]==s3[p3]:
#                     p2 += 1
#                     p3 += 1
#                 else:
#                     return self.helper(s1[p1+1:],s2[p2:],s3[p3+1:]) or self.helper(s1[p1:],s2[p2+1:],s3[p3+1:])
#             elif p1 < length1 and p2 >= length2:
#                 if s1[p1]!=s3[p3]:
#                     return False
#                 else:
#                     p1 += 1
#                     p3 += 1
#             elif p1 >= length1 and p2 < length2:
#                 if s2[p2]!=s3[p3]:
#                     return False
#                 else:
#                     p2 += 1
#                     p3 += 1
#             else:#这种情况其实是不存在的，因为最开始已经进行了长度判断
#                 return False
#         return True
#==============================================================================
        
s = Solution()
s1 = "baababbabbababbaaababbbbbbbbbbbaabaabaaaabaaabbaaabaaaababaabaaabaabbbbaabbaabaabbbbabbbababbaaaabab"
s2 = "aababaaabbbababababaabbbababaababbababbbbabbbbbababbbabaaaaabaaabbabbaaabbababbaaaababaababbbbabbbbb"
s3 = "babbabbabbababbaaababbbbaababbaabbbbabbbbbaaabbabaababaabaaabaabbbaaaabbabbaaaaabbabbaabaaaabbbbababbbababbabaabababbababaaaaaabbababaaabbaabbbbaaaaabbbaaabbbabbbbaaabaababbaabababbbbababbaaabbbabbbab"
print s.isInterleave(s1,s2,s3)