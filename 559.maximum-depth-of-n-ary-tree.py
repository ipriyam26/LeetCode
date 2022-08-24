#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:

        def maxDepth(self, root: 'Node') -> int:
            if root is None:
                return 0
            depth = 0
            for child in root.children:
                depth = max(depth, self.maxDepth(child))
            # print(f'root {str(root.val)} depth {str(depth + 1)}')
            return depth + 1 
        
# @lc code=end

