#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:35:39 2020

@author: andrew
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits
            digits[i] = 0
        digits.insert(0,1)
        return digits
#       list的倒循环 不为9 +1返回 如果为9 下一个循环 再+1 如果都循环完 都为9 则插入到首位一个1

        # for i in range(1,len(digits)+1):
        #     if digits[-i] != 9:
        #         digits[-i] += 1
        #         return digits
        #     digits[-i] = 0
        # digits.insert(0,1)
        # return digits