#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        q = [root]
        while q:
            curr = q.pop(0)
            if curr.val != val:
                return False
            if curr.left:
                q.insert(0,curr.left)
            if curr.right:
                q.insert(0,curr.right)
        return True
        