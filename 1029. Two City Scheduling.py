#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:27:41 2020

@author: andrew
"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
# 此题一定要详细读题，2N个人 N个人去一个城市 另外N去另外一个城市，所以差价价格进行排序 前一半去A 后一半去B
        return sum(list(v[0] if i < len(costs) // 2 else v[1]  for i, v in enumerate(list(sorted(costs, key = lambda costs : costs[0] - costs[1])))))