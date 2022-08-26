#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def find(self,node:TreeNode,path:str) -> List[str]:
        if not node.left and not node.right:
            return [path+str(node.val)]
        
        Lstr,Rstr = [],[]
        if node.left:
            Lstr = self.find(node.left,path+str(node.val))
        if node.right:
            Rstr = self.find(node.right,path+str(node.val))
        return Lstr+Rstr
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root:
            res = self.find(root,'')
            return sum(int(i,2) for i in res)
        else:
            print("Empty")
        
# @lc code=end

