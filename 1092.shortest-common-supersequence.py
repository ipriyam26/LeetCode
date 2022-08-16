#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence 
#

# @lc code=start
import contextlib
from typing import List


class Solution:
    
    
    def make_top_down(self,S1: str  ,S2:str ,n: int,m: int) -> List[List[int]]:
        dp = [[None]*(n+1)for _ in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif S2[i-1]==S1[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp
    
    def find_lcs(self,S1: str  ,S2:str ,n: int,m: int,dp:List[List[int]]) -> str:
        lcs=""
        i=m
        j=n
        while (i>0 or j>0):
            if (S2[i-1]==S1[j-1]):
                lcs=S2[i-1]+lcs
                i -= 1
                j -= 1
            elif (dp[i-1][j]>dp[i][j-1]):
                i -= 1
            else:
                j -= 1    
        
        return lcs
    def find_non_occuring(self, S:str, lcs:str):
        ll = S.split()
        for element in lcs:
            with contextlib.suppress(Exception):
                ll.pop(element)
        return "".join(ll)
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp  = self.make_top_down(str1,str2,len(str1),len(str2))
        lcs = self.find_lcs(str1,str2,len(str1),len(str2),dp)
        s1 = self.find_non_occuring(str1,lcs)
        s2 = self.find_non_occuring(str2,lcs)
        print(s1)
        print(s1)
        print(lcs)
        return s1+lcs+s2
    
        
# @lc code=end

