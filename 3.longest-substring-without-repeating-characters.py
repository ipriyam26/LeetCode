#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = -1,0
        max_value = 0
        holder = {}
        while j <len(s):
            # holder[s[j]]+=1
            # if (j-i+1==len(holder)):
            #     if(j-i+1>max_value):
            #         max_value = j-i+1
            # else:
            #     while(j-i+1!=len(holder)and i<j):
            #         holder[s[i]]-=1
            #         if holder[s[i]]==0:
            #             holder.pop(s[i])  
            #         i+=1
            # j+=1
            if(s[j] in holder and holder[s[j]]>i):
                i = holder[s[j]]
            elif j-i > max_value:
                max_value=j-i
            holder[s[j]]=j
            j+=1
        return max_value
            
            
        
        
# @lc code=end

