#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 13:57:51 2020

@author: andrew
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            # print (stack)
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
        # 解题思路是把root变成一个list (缺点：需要整个root都转换成数组后得出结果)
#         def tolist(r):
#             return tolist(r.left) + [r.val] + tolist(r.right) if r  else []
        
#         return tolist(root)[k-1]
