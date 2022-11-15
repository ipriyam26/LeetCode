#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    
    def tryMe(self,s:str,i:int,j:int):
        
        if self.memo[s[i:j]]==-1:
            return False
        if self.dc[s[i:j]]==1:
            return True
        
        for k in range(i+1,j):
            
            if self.dc[s[i:k]] and self.tryMe(s,k,j):
                return True
        
        self.memo[s[i:j]] = -1
        return False
        
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = defaultdict(lambda:0)
        self.dc = defaultdict(lambda:0)
        for word in wordDict:
            self.dc[word]=1
            
        return self.tryMe(s,0,len(s))

        
# @lc code=end

