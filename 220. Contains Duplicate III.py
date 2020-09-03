#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:36:28 2020

@author: andrew
"""

#此题可以理解为 k是一个窗口 

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        from sortedcontainers import SortedSet
        if not nums or t < 0: return False     
        ss, n = SortedSet(), 0                 # 设置一个set 去控制这个set大小在k之间的窗口范围
        for i, num in enumerate(nums):
            ceiling_idx = ss.bisect_left(num)  # 找到set的数组里第一个大于 num[i]的值  
            floor_idx = ceiling_idx - 1        # 找到set的数组里第一个小于 num[i]的值
            if ceiling_idx < n and abs(ss[ceiling_idx]-num) <= t: return True  # 查看ceiling是否符合要求 
            if 0 <= floor_idx and abs(ss[floor_idx]-num) <= t: return True     # 查看floor是否符合要求
            ss.add(num) #把新数添加到set 
            n += 1
            if i - k >= 0:  # 判断set是否超过长度k 确保长度符合k要求
                ss.remove(nums[i-k])
                n -= 1
        return False