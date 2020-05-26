#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:58:05 2020

@author: andrew
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dic = collections.Counter(nums1)
        nums2_dic = collections.Counter(nums2)
        ans = []
        dic= nums1_dic if len(nums1_dic) < len(nums2_dic) else nums2_dic
        dic_long = nums1_dic if len(nums1_dic) >=len(nums2_dic) else nums2_dic
        for k in dic.keys():
            if k in dic_long.keys():
                ans.append(k)
        return ans