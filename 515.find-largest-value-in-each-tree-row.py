#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        q = [root]
        result = []
        while q:
            size = len(q)
            result.append(max(res.val for res in q))
            for _ in range(size):
                element = q.pop(0)
                if element.right:
                    q.append(element.right)
                if element.left:
                    q.append(element.left)
        return result   
            

        
# @lc code=end

