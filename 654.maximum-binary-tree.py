#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==1:
            return TreeNode(nums[0])
        index = self.find_max_index(nums)
        root = TreeNode(nums[index])
        if index!=0:
            root.left = self.constructMaximumBinaryTree(nums[:index])
        if index!=len(nums):
            root.right = self.constructMaximumBinaryTree(nums[index+1:])
        return root
        
    def find_max_index(self,arr:List[int]):
        return arr.index(max(arr))
        
# @lc code=end

