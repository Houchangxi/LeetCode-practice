#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 12:20:16 2020

@author: andrew
"""

from itertools import permutations
import sys
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        per = list(permutations(A,4))
        max_time = -1
        for i in per:
            num_hour = i[0]*10+i[1]
            num_min = i[2]*10+i[3]
           
            if num_hour < 24 and num_min < 60:
                max_time = max(max_time, num_hour*60+num_min)
        result = ""
        if max_time>=0:
            result = "{:02d}:{:02d}".format(max_time // 60, max_time % 60)
        
        return result