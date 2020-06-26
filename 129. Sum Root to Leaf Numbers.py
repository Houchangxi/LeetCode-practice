#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:48:54 2020

@author: andrew
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root ==None:
            return 0
        path = ''
        group = []
        def helper(root,path,group):
            path = path+str(root.val)
            if root.left == None and root.right ==None:
                group.append(path)
                return
            if root.left is not None:
                helper(root.left,path,group)
            if root.right is not None:
                helper(root.right,path,group)
        helper(root,path,group)
        return sum([int(x) for x in group])