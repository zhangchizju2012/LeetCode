#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 19:47:02 2017

@author: zhangchi
"""
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        self.s1 = s1
        self.s2 = s2
        self.result = {(0,0):0}
        length1 = len(s1)
        length2 = len(s2)
        for i in xrange(1,length1+1):
            self.result[(i,0)] = ord(s1[i-1]) + self.result[(i-1,0)]
        for i in xrange(1,length2+1):
            self.result[(0,i)] = ord(s2[i-1]) + self.result[(0,i-1)]
        return self.helper(length1,length2)
            
    def helper(self,i,j):
        if (i,j) not in self.result:
            if self.s1[i-1] == self.s2[j-1]:
                self.result[(i,j)] = self.helper(i-1,j-1)
            else:     
                self.result[(i,j)] = min(self.helper(i-1,j)+ord(self.s1[i-1]),\
                                        self.helper(i,j-1)+ord(self.s2[j-1]))
            
        return self.result[(i,j)]

# =============================================================================
# class Solution(object):
#     def minimumDeleteSum(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: int
#         """
#         result = {(0,0):0}
#         length1 = len(s1)
#         length2 = len(s2)
#         for i in xrange(1,length1+1):
#             result[(i,0)] = ord(s1[i-1]) + result[(i-1,0)]
#         for i in xrange(1,length2+1):
#             result[(0,i)] = ord(s2[i-1]) + result[(0,i-1)]
#         for i in xrange(1,length1+1):
#             for j in xrange(1,length2+1):
#                 if s1[i-1] == s2[j-1]:
#                     result[(i,j)] = result[(i-1,j-1)]
#                 else:     
#                     result[(i,j)] = min(result[(i-1,j)]+ord(s1[i-1]),\
#                                         result[(i,j-1)]+ord(s2[j-1]))
#         return result[(length1,length2)]
# =============================================================================
            
            
s = Solution()
#print s.minimumDeleteSum("sea", "eat")
#print s.minimumDeleteSum("delete","leet")
#print s.minimumDeleteSum("","")
#a = "zyomgwqaoninimjmgrvlubqjhrzuhooukkytlrymjjqeiusguxgssjiozmvxgndcukmstsdrefhrtwqvcqtxvtapszxryazsrguszwitukccbxwjqucorvyerxvpalrpvockrfxntwsktjumkmjohknviqhuvzmnqowqazjnwedtavxxxaitcgwnnhulhqzqybgfwgapjuxjysygpcnomedaoyjywjpkijahfcwpwjjzgoczugl"
#b = "vlhxdnzgaojwsyzdghjgplbidswfniohpdsrczbililhubozfzjstqrnkonbpyykssdvwugcnmsqasnxylgtnuygoacnwevqbjtvyisdojnotjjrifnnmojjcgpeglqejyerhywkmuyppfscbybcjusralaosqvkhceuolvaxwrehigvdvojkyueudnwzukgijagauxyblnuajifvcsaqelotezbfecircokqhhpqoyjrzqdvuyqvscgjuehtuygbraawzqqpaqeqfxiffaunilooccmrihjoosakmxlhsmiokpmlehigqbxblzkjyzwmxsuiutubpmoravvftwhtudrprmwzvszgoqyyythptkhgscdypwcocdfpuxspdc"
a = "llrseubegfbbforocgnpemtubqiumwgfmgdkhjtsyjbndtgbxdkwzzockdntxkipkpcaqetreyhrubneiidagirzvsqjhirdcyqbxjsxqfuhmblkqszlkhmvhlhwvworivjtagkvhrfhgeeeevvcsiygyfpeepmxekvhkuryjpsckilzvgpdfkcmqcmrpxvnazdodlsgftggehzltfsarvjexpgvzqnwzlbeeagakyrvaylgjyfautcnubojohvfbzziaudfkloxcelmqwzwqvlwmfmjqmkzcztceoxsakfmjfpwfvhmurvrkouavxgxkdepvzktttthfakppkipwdnpwjgrmywtxwtnsfwaawsljgychkgpwmuoywizqcwppyqzaevgmefudmoabxnjnnuibdiwocwaqoitltgwnbpqfajkuzbescdlrzltaxjrfajbnqe"
b = "qkynliglsdnadlyoofjcvwcrwuuqjoqqobyebajhyakcbxqjzdntluzjjktukbxrpqnebnquplklpzkyfjnqeoicukwimvknxevvuzminepdltysbmkgcgpfzqddzgrohpqtlbqxujfetgjcbyqrtwjczrfcngcmuykruwaypcscujrhecjeualpswrtptxbommmvmayehpmfmyerjwoaohexrorqntvkqemdrqhlmjymtus"
print s.minimumDeleteSum(a,b)