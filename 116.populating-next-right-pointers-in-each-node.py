#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""



class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr, nxt = root, root.left if root else None
        while curr and nxt:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
            if not curr:
                curr = nxt
                nxt = curr.left
        return root    
                
            
        
# @lc code=end

