#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import DefaultDict, List, Optional


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.table = defaultdict(list)
        self.order(root)
        ans = [values[0] for  values in self.table if len(values) > 1]
        ans.reverse()
        return ans
                
                
    
    def order(self,root):
        if not root:
            return "None"
        res = f"{root.val} {self.order(root.left)} {self.order(root.right)}"
        self.table[res].append(root)
        return res
    
        
        
# @lc code=end

