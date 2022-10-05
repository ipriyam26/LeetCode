#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # counter = Counter(t)
        if len(t)>len(s):
            return ""
        if len(t)==1 and t in s:
            return t
        
        hashDict = defaultdict(int)
        for charr in t:
            hashDict[charr]+=1
        i,j=0,0
        ans = len(s)
        ansString = ""
        count = len(hashDict)
        while j <len(s):
            if s[j] in hashDict:
                hashDict[s[j]]-=1
                if hashDict[s[j]]==0:
                    count-=1
            if count==0:
                if ans > j-i+1:
                    ans = j-i+1
                    ansString = s[i:j+1]     
                # run=0
                while count==0 and i<j:
                    # run=1
                    if s[i] in hashDict:
                        hashDict[s[i]]+=1
                        if hashDict[s[i]]>0:
                            count+=1
                    i+=1
                    
                if ans > j-i:
                    ans = j-i
                    ansString = s[i-1:j+1]  
            j+=1
        return ansString
                
                    
                
        
        
        
# @lc code=end

