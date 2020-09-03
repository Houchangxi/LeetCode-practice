#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:39:00 2020

@author: andrew
"""

#此题一行代码，主要表达的是是否 有重复，如果将原字符串copy 叠加之后  剔除掉第一个和最后一个字符 原字符串依然存在于叠加后字符串 即可认为为重复字符串
#证明看 https://www.youtube.com/watch?v=46FlH2Kj1LI
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]