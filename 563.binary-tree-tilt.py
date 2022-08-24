#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    
    def find(self,root: Optional[TreeNode]):
        if not root:
            return 0
        left = self.findTilt(root.left)
        right = self.findTilt(root.right)
        curr = root.val
        root.val = abs(left - right)
        print(root.val,"For current ->",curr)
        self.total += root.val
        return curr + left + right
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.find(root)
        return self.total

    
        
         
        
# @lc code=end

