#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root : return []
        results = self.find(root=root,targetSum=targetSum,selected=[])
        results = [result for result in  results if result]
        return results
             
    
    def find(self, root: TreeNode, targetSum: int, selected: List[int]) -> List[List[int]]:
        if not root.left and not root.right:
            return [] if root.val != targetSum else [selected + [root.val]]
        res1, res2 = [[]], [[]]
        if root.left:
            res1 = self.find(root=root.left, targetSum=targetSum - root.val, selected=selected + [root.val])

        if root.right:
            res2 = self.find(root=root.right, targetSum=targetSum - root.val, selected=selected + [root.val])

        print(f"{res1} and {res2} for {root.val}")
        return res1 + res2
        
# @lc code=end

