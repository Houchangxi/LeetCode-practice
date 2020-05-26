#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 18:26:45 2020

@author: andrew
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root,]
        ans = []
        while stack:
            node = stack.pop()
            if node is not None:
                ans.append(node.val)
                if node.right is not None:
                    stack.append(node.right)

                if node.left is not None:
                    stack.append(node.left)
        return ans
    
    
#     这个题 牢记 1、preorder 前序遍历  root - left - right  这个顺序进行二叉树遍历， 因为用的是stack的iteraction去做 所以要用到先进后出（FILO）所以 压栈的时候先压 right 然后压left （root right left）
# inorder left - root - right 
# postorder left - right - root