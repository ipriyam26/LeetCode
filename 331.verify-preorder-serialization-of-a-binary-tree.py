#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        left_nodes = 1
        for node in preorder.split(','):
            left_nodes-=1
            if (left_nodes<0):
                return False
            if (node!='#'):
                left_nodes+=2
        return left_nodes==0
        
# @lc code=end

