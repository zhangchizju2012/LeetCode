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

#0919
11. 穷举是n^2复杂度，为了达到n复杂度，最关键的是，不能把最终答案的那种给漏了，别的漏了都无所谓
    采用two pointers的思路，pointer移动的策略是，所对应的值小的pointer进行移动，大的不移动
    证明这种策略不会错过答案：
    假设两个pointer中的一个先抵达了结果中矮的那个，另一个pointer对应的杆子肯定矮一些，且在抵达结果中高的那个之前，不会碰到比结果中矮的那个要高的棍子，否则这一对就是结果了
    假设两个pointer中的一个先抵达了结果中高的那个，另一个pointer对应的杆子对应的杆子肯定比结果中矮的那个要矮，且在抵达结果中矮的那个之前，碰到的棍子都比那个矮的要矮
14. 简单，扫描所有string,找最小长度，然后一个字符一个字符扫描过去
15. 基本思路是一个一个扫描，剩下的按照2sum来，这样复杂度是n^2
    然后可以先sort一下，然后超过三个的没有意义，然后其实sort了之后，对于剩下的，也可以考虑用two pointer
    来做，小了一个pointer移动，大了另一个pointer移动（像google interview里的）
16. sort, 一个for loop, 后面two pointers，像上题一样
17. it can be solved recursively
    也可以不recursive, for loop 一个一个扫描，搞个result, 搞了temp, result储存在第i个时的结果，temp储存下一个结果，不断用temp更新result
19. 两个指针，第二个pointer在第一个移动n步之后开始移动

#0920
20. stack 简单
21. 简单，注意linked list的用法
22. bfs/dfs ? 应该是dfs，能走的都先走掉 （又重写了一遍）
23. 再复习，用heapq
24. 创建first, second, third 分别对应后续三个需要处理的node（手写了代码）
25. <Reverse Nodes in k-Group> 类似24，但是放在list里，这样就可以扫描很多个了 (但是这样的space complexity会与k有关)

#0921
26. <Remove Duplicates from Sorted Array> 简单，重新手写了代码
27. <Remove Element> 简单，像26
28. 弱智，the length of ... is not necessarily 1
30. <Substring with Concatenation of All Words> 再复习
    最基本思路：每个单词长度是a,总共b个单词，然后就有个长度为ab的窗口，去扫描整个string,然后与list里的内容比较
    改进：但是这样的话，很多进行了重复运算，不好。对于每个string, **********，(假设单词长度为3）可以
    这样划分：***|***|***|*，*|***|***|***|,然后对每个部分去看是否存在于dict里，这样可以避免重复运算 （可以做一下）
亚麻oa 3题