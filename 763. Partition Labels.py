#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:34:38 2020

@author: andrew
"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
#         1、遍历数组，获取每一个字母最后一次出现的index
#         2、设置一个快慢指针 pre cur，遍历数数组，
#         3、如果现在的字母最后一位的index 和目前遍历的字母进行比较 大于就更新cur。等于久说明找到一个分割点进行分割
#         如:{'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}
#         b:5<a:8  cur = 8  c:7<a:8  cur = 8 直到数组第8位 cur==i 此处为分割点 add ans中

        # 获取每个字母最有一位index
        element_last_index  =  {c:i for i,c in enumerate(S)}

        pre = cur =0
        ans = []
        for i,c in enumerate(S):
            cur = max(cur,element_last_index[c])
            if cur == i:
                ans.append(cur-pre +1)
                pre = cur + 1
        return ans