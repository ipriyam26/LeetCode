#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.dp = [[-1 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        return self.findDistinct(len(s)-1,len(t)-1,s,t)
    
    def findDistinct(self,i:int,j:int,s:str,t:str) -> int:
        if j<0:
            return 1
        if i<0:
            return 0
        if self.dp[i][j]!=-1:
            return self.dp[i][j]
            
        if s[i]==t[j]:
            self.dp[i][j]= self.findDistinct(i-1,j-1,s,t) + self.findDistinct(i-1,j,s,t)
        else:
            self.dp[i][j]= self.findDistinct(i-1,j,s,t)
        return self.dp[i][j]

        
        
        
# @lc code=end

