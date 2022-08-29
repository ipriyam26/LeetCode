#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
     
        def recurse_tree(current_node):
            if not current_node:
                return False
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            mid = current_node in [p, q]
            if mid + left + right >= 2:
                self.ans = current_node
            return mid or left or right

        recurse_tree(root)
        return self.ans
        
# @lc code=end

