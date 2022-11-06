#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s),len(t)
        self.dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            self.dp[i][0]=1 
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==t[j-1]:
                    self.dp[i][j]= self.dp[i-1][j-1] + self.dp[i-1][j]
                else:
                    self.dp[i][j]=self.dp[i-1][j]
        return self.dp[n][m]

        
        
        
# @lc code=end

