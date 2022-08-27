#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import  List, Optional

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root] 
        ans = []
        while q:
            curr = len(q)
            ans.append(q[curr - 1].val)
            for _ in range(curr):
                elem = q.pop(0)
                if elem.left:
                    q.append(elem.left)
                if elem.right:
                    q.append(elem.right)
        return ans
# @lc code=end

