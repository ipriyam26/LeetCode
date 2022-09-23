#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,0
        max_value = 0
        holder = set()
        while j <len(s):
            holder.add(s[j])
            if (j-i+1==len(holder)):
                if(j-i+1>max_value):
                    max_value = j-i+1
            else:
                while(s[i]!=s[j] and i<j):
                    i+=1
                    holder.remove(s[i])
                i+=1
            j+=1
        return max_value
            
            
        
# @lc code=end

