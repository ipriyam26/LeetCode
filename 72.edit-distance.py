#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def findMinium(self,i:int,j:int,word1:str,word2:str):
        #base condition
        if i<0 and j<0:
            return 0
        if i<0:
            return 1+ j
        if j<0:
            return 1 + i

        if self.dp[i][j]!=-1:
            return self.dp[i][j]
        
        if word1[i]==word2[j]:
            self.dp[i][j]= self.findMinium(i-1,j-1,word1=word1,word2=word2)
        else:
            self.dp[i][j]=  1 + min(self.findMinium(i-1,j,word1=word1,word2=word2) , self.findMinium(i,j-1,word1=word1,word2 = word2), self.findMinium(i-1,j-1,word1=word1,word2=word2))
        return self.dp[i][j]
        

    def minDistance(self, word1: str, word2: str) -> int:
        self.dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
        n,m = len(word1),len(word2)
        for j in range(m):
            self.dp[0][j]=j
        for i in range(n):
            self.dp[i][0]=i
        
        self.dp[0][0]=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    self.dp[i][j] = self.dp[i-1][j-1]
                else:
                    self.dp[i][j] = 1+ min( self.dp[i-1][j],self.dp[i][j-1], self.dp[i-1][j-1])
        print(self.dp)
        return self.dp[n][m]
        
         

        
# @lc code=end

