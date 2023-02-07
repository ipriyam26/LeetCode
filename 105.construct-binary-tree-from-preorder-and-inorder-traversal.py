#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            indexRoot = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[indexRoot])
            root.left = self.buildTree(preorder, inorder[:indexRoot])
            root.right = self.buildTree(preorder, inorder[indexRoot + 1 :])
            return root


# @lc code=end
