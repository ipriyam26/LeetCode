#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = [root]
        p=[]
        cd = 1
        while q:
            size=len(q)
            p=[]
            for _ in range(size):
                ele = q.pop(0)
                p.append(ele)
                
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
                
            cd+=1
        print(p)
        return p.pop(0).val
        
# @lc code=end

