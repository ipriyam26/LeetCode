#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        result = ""
        # lets doo bfs
        while queue:

            i=0
            curr_l = len(queue)
            while i<curr_l:
                element = queue.pop(0)
                i+=1
                if not element:
                    result+="X "
                    continue
                result += f"{str(element.val)} "
                queue.extend((element.left, element.right))
        print(result)
        return result
            
                
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        queue = [0]
        root = TreeNode(data[0])
        while queue:
            i=0
            curr_len = len(queue)
            while i<curr_len:
                element = queue.pop(0)
                
                
                
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

