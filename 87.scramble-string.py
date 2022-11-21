#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
class Solution:
    def make_result(self,s:str,i:int,j:int):
        if j-i==1:
            return {s[i:j]}

        if self.dp[i][j]:
            return self.dp[i][j]

        result=set()
        for k in range(i+1,j):
            lefts = self.dp[i][k] or self.make_result(s,i,k)
            rights = self.dp[k][j] or self.make_result(s,k,j)
            for left in lefts:
                result.update([left + right for right in rights])
                result.update([right + left for right in rights])
                
        self.dp[i][j].update(result)
        return self.dp[i][j]
    
    def isScramble(self, s1: str, s2: str) -> bool:
        self.dp = [[set() for _ in range(len(s1)+1)] for _ in range(len(s1)+1)]
        results = self.make_result(s1,0,len(s1))
        print(results)
        return s2 in results
        
        

        
# @lc code=end

