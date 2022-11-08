#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:

    def matches(self,i:int,j:int,s:str,p: str):
        if j<0:
            return i<0
        if i<0:
            return p[j]=="*" and self.matches(i,j-1,s,p)
        
        if self.dp[i][j] != None:
            return self.dp[i][j]
            
        if s[i] != p[j] and p[j] != '?' and p[j] == "*":
            self.dp[i][j]= self.matches(i,j-1,s,p) or self.matches(i-1,j,s,p)
        elif s[i] != p[j] != '?':
            self.dp[i][j] = False

        else:
            self.dp[i][j]= self.matches(i-1,j-1,s,p)
        return self.dp[i][j]
                    
                
            
    def isMatch(self, s: str, p: str) -> bool:
            self.dp = [[None for _ in range(len(p)+1)] for _ in range(len(s)+1)]
            return self.matches(len(s)-1,len(p)-1,s,p)
        
# @lc code=end

