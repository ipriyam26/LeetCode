#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    
    def insert(self,root,value):
        if not root:
            return TreeNode(val=value)
        if root.val<value:
            self.insert(root.right,value)
        else
    
    def trees(self,root:TreeNode,leftover:List[int]):
        
    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        pass
        
# @lc code=end

