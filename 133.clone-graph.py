#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import defaultdict, deque


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft() 
            cur_clone = clones[cur.val]            

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                    
                cur_clone.neighbors.append(clones[ngbr.val])
                
        return clones[node.val]
                
            
        
# @lc code=end

