#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 08:51:17 2020

@author: andrew
"""
import collections
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        # counts = collections.Counter(s)
        # return ''.join(i*times for i, times in counts.most_common())
#     collections.Counter会直接按照统计完成的字母数降序排列，然后most_common是获取最多的前几个字母 不填写为全部取出
        
        counts = collections.Counter(s)
        h = [(v,k) for k,v in counts.items()]
        print(heapq.nlargest(len(h),h))
        return "".join(k*v for k,v in heapq.nlargest(len(h),h))
#     counter 统计完成后 也可以用 heapq的 nlargest 进行元组排序 转换成string