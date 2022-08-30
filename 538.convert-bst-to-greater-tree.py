#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
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
    
    def makeAns(self,root,val):
        if not root.left and not root.right:
            root.val = root.val+val
            return root.val
        if root.right:
            val = self.makeAns(root.right,val)
        root.val = root.val + val
        if root.left:
            lft = self.makeAns(root.left,root.val)
            return lft
        return root.val
        
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        self.makeAns(root,0)
        return root
        
# @lc code=end

