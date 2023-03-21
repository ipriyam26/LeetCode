#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        needed_letters = Counter(t)
        needed_len = len(t)
        minimum_window = ""
        start=0
        for end in range(len(s)):
            
            if needed_letters[s[end]]   >0:
                needed_len-=1
            
            needed_letters[s[end]]-=1
            
            while needed_len==0:
                window_len = end-start+1
                
                if not minimum_window or window_len < len(minimum_window):
                    minimum_window = s[start:end+1]
                
                needed_letters[s[start]]+=1
                
                if needed_letters[s[start]] > 0:
                    needed_len+=1
                start+=1
                
        return minimum_window
                
                
                
                
            
                
                    
                
        
        
        
# @lc code=end

