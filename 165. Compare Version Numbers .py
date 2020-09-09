#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:33:19 2020

@author: andrew
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        l1 = len(v1)
        l2 = len(v2)
        lr = max(l1,l2)
        for i in range(lr):
#             此处的int 转换 过滤调 01 002 这样的字符串
            c1 = int(v1[i]) if i<l1 else 0
            c2 = int(v2[i]) if i<l2 else 0

            if c1 != c2:
                return 1 if c1>c2 else -1
        return 0
                