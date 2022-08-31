#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        ans = []
        zig = True
        while  q:
            size = len(q)
            curr = []
            for _ in range(size):
                element = q.pop(0)
                if zig:
                    curr.append(element.val)
                else:
                    curr.insert(0, element.val)
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
            ans.append(curr)
            zig = not zig
        return ans
    
        
        
# @lc code=end

