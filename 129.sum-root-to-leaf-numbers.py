#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
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
    
    def dfs(self,root,current="")->List[int]:
        if not root.left and not root.right:
            return [int(current+str(root.val))]
        result = []
        if root.left:
            result += self.dfs(root.left,current=current+str(root.val))
        if root.right:
            result += self.dfs(root=root.right,current=current + str(root.val))
        return result
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numbers = self.dfs(root=root)
        return sum(numbers)
        
# @lc code=end

