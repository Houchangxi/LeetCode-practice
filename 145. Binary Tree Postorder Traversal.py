#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:54:51 2020

@author: andrew
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root,]
        ans = []
#         postorder  left-right-root
#         postorder的逆序 root - right -left 这个和preorder root-left -right 只需要把左右的位置调换 
#         所以解法是 求 root -left - right 然后逆序就可以得到postorder
        while(len(stack)>0):
            root = stack.pop()
            if root is not None:
                ans.append(root.val)                
                if root.left is not None:
                    stack.append(root.left)
                if root.right is not None:
                    stack.append(root.right)
        return reversed(ans)