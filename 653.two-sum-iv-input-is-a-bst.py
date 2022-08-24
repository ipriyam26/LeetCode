#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

# [5,3,6,2,4,null,7]
# 28

class Solution:
    


    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack, seen = [root], set()
        
        while stack:
            curr = stack.pop()
            # If we've seen k - curr.val,
            # we have k - curr.val + curr.val = k
            if k - curr.val in seen:
                return True
            seen.add(curr.val)
            
            # Visit children
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
                
        return False
        
# @lc code=end

