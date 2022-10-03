#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import defaultdict



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j=0,0
        max_count = 0
        holder = defaultdict(int)
        # count=0
        while j < len(s):
            holder[s[j]]+=1
            # if len(holder)<=k:
            #     pass
            tbc = sum(holder.values()) - max(holder.values())
            if tbc<=k and max_count < j - i + 1:
                max_count=j-i+1
            elif(tbc>k):
                while tbc>k and i<j:
                    
                        
                    i+=1
            j+=1


        return max_count
        
# @lc code=end

