#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
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
    
    def dfs(self, root: TreeNode, depth: int) -> int:
        if depth > self.global_min:
            return self.global_min
        if root.left is None and root.right is None:
            self.global_min = min(self.global_min, depth + 1)
            return depth + 1
        
        left,right = 1000001,1000001
        if root.left :
            left = self.dfs(root.left, depth + 1)
        if root.right :
            right = self.dfs(root.right, depth + 1)
        return min(left, right)
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.global_min = 1000001
        return 0 if root is None else self.dfs(root, 0)
        

        
# @lc code=end

