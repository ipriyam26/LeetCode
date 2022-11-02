#
# @lc app=leetcode id=1312 lang=python3
#
# [1312] Minimum Insertion Steps to Make a String Palindrome
#

# @lc code=start
import itertools
class Solution:
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text2)
        n = len(text1)
        self.dp = [[ -1 for _ in range(m+1)] for _ in range(n+1)]
        for i in range (n+1):
            self.dp[i][0]=0

        for j in range(m+1):
            self.dp[0][j] =0

        i,j=0,0
        for i, j in itertools.product(range(1,n+1), range(1,m+1)):
            if text1[i-1] == text2[j-1]:
                self.dp[i][j] = self.dp[i - 1][j - 1] +1 
            else:
                self.dp[i][j]=max(self.dp[i - 1][j], self.dp[i][j - 1])

        return self.dp[n][m]
    
    def minInsertions(self, s: str) -> int:
        return len(s)-self.longestCommonSubsequence(s,s[::-1])
        
        
# @lc code=end

