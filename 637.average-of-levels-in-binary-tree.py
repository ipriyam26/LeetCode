#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
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
    
    def solve(self,root,level):
        if not root: return []
        if level not in self.res:
            self.res[level] = [root.val]
        else:
            self.res[level].append(root.val)
        self.solve(root.left, level+1)
        self.solve(root.right, level+1)
        return [sum(self.res[level])/len(self.res[level]) for level in self.res]
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.res = {}
        return self.solve(root, 0)
# @lc code=end

