#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:14:10 2020

@author: andrew
"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for i in people:
            res.insert(i[1], i)
        return res
#         // 先排序  先按照身高倒序 再在每个身高里按照升序排前面人数的序
#         // [7,0], [7,1], [6,1], [5,0], [5,2], [4,4]
        
#         // 再一个一个插入。按照身高的前边几个人 作为index 插入队列即可
#         // [7,0]
#         // [7,0], [7,1]
#         // [7,0], [6,1], [7,1]
#         // [5,0], [7,0], [6,1], [7,1]
#         // [5,0], [7,0], [5,2], [6,1], [7,1]
#         // [5,0], [7,0], [5,2], [6,1], [4,4], [7,1]