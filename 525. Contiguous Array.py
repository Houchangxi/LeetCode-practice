#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 13:31:25 2020

@author: andrew
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counter = {}
        sum_record = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i]==1:
                sum_record +=1
            else:
                sum_record -=1
            if sum_record ==0:
                ans=i+1
            if sum_record not in counter:
                counter[sum_record] = i
            else:
                ans = max(ans,i-counter[sum_record])
        return ans
    
#     用字典或者认为是hashmap去记录第一次出现和的index值  0则-1 1则1 求sum 只要出现2个相同的sum值 则认为新的index和之前存储的index直接的 list长度是最长的 subarray 含有0，1的  