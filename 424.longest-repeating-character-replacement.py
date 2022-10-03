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
            if len(holder) <= k + 1 and max_count < j - i + 1:
                max_count=j-i+1
            elif(len(holder)>k+1):
                while len(holder)>k+1:
                    holder[s[i]]-=1
                    if(holder[s[i]]==0):
                        holder.pop(s[i])
                    i+=1
            j+=1


        return max_count
        
# @lc code=end

