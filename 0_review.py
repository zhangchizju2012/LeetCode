#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 00:45:06 2017

@author: zhangchi
"""


# 0918
2. 简单
3. 用两个dic来做查询和删除，会比find好，此题是因为只有26个字母所以find也不算太慢
    用一个dic应该也可以，之后更新的时候更新一个variable，这个variable里储存目前的substring的起始index
    然后做查询的时候，检查index是否存在，且在这个index之后
5. 要继续复习! 
    temp储存扫描到第i个字符前的结果, 而不是从第i字符开始往后的结果
6. 其实就是以（2n-2）为一个单位 （可以试着做做）感觉是比较烦的
7. 先确定正负，变成str，然后[::-1]倒过来，再变成int，再判断有没有大于等于2**31 
  （因为总共32位，一位符号位，从0到30共31个，全为1，下一个数就是2**31）
8. 要继续复习! 
    这道题没什么意义 https://discuss.leetcode.com/topic/31602/this-problem-is-meanless
    实际上应该问的是用constant memory （但是不要直接去转str）
    这个思路不错：去掉原式子的后一半，然后用后一半去建新的，比较新的和原式子的前一半是否一致，可以避免overflow问题