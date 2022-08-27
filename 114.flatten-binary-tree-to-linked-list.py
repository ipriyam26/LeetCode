#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
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

    def fix(self,root:TreeNode)->TreeNode:
        if not root.left and not root.right:
            return root
        # Getting the left side of tree
        left,right = None,None
        if root.left:
            left = self.fix(root.left)
        # Getting the right side of the current
        if root.right:
            right = self.fix(root.right)
        # Removing left connections
        root.left = None
        root.right = left
        # Going to the end of left branch
        temp = root
        while temp.right:
            temp = temp.right
        # Adding right branch to the right of temp node which is at the 
        # end of left by now
        temp.right = right 
        # returning root to the stack to add more values to it
        return root
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            root = self.fix(root=root)
        
# @lc code=end

