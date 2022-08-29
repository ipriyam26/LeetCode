#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        if not root: 
            return root
        if root.val > key: 
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right: 
                return root.left
            if not root.left: 
                return root.right
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val 
            root.right = self.deleteNode(root.right,root.val) 
        return root
        
# @lc code=end

