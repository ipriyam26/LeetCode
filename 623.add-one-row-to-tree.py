#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
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
    
    
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            n = TreeNode(val)
            n.left = root
            return n
        self.insert(root,val,1,depth)
        return root
    
    def insert(self,root,val,depth,n):
        if not root:
            return
        
        if depth==n-1:
            T = root.left
            root.left = TreeNode(val)
            root.left.left = T
            T = root.right
            root.right = TreeNode(val)
            root.right.right = T
        else:
            self.insert(root.left,val,depth+1,n)
            self.insert(root.right,val,depth+1,n)
    
        
        
        
        
        
# @lc code=end

