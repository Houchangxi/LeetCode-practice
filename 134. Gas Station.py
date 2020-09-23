#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:03:31 2020

@author: andrew
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 判断是否有解 整体gas是否涵盖整体cost
        if sum(gas)<sum(cost):return -1
        ind_now,oil_now = 0,0
        #查找index 
        for i in range(len(gas)):
            if oil_now + gas[i] < cost[i]:
                ind_now = 1 + i
                oil_now = 0
            else:
                oil_now += gas[i] - cost[i]
        return ind_now