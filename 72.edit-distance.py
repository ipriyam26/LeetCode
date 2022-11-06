#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def findMinium(self,i:int,j:int,word1:str,word2:str):
        if i<0:
            return 1 if j<0 else 1+ self.findMinium(i,j-1,word1=word1,word2=word2)
        if j<0:
            return 1 + self.findMinium(i-1,j,word1=word1,word2=word2)
        
    
    def minDistance(self, word1: str, word2: str) -> int:

        
# @lc code=end

