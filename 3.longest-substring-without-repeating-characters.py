#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from collections import defaultdict


class Solution:
    def default_fill():
        return 0
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,0
        max_value = 0
        holder = defaultdict(self.default_fill)
        while j <len(s):
            holder[s[j]]+=1
            if (j-i+1==len(holder)):
                if(j-i+1>max_value):
                    max_value = j-i+1
            else:
                while(j-i+1!=len(holder)and i<j):
                    holder[s[i]]-=1
                    if holder[s[i]]==0:
                        holder.pop(s[i])  
                    i+=1
            j+=1
        return max_value
            
            
        
# @lc code=end

