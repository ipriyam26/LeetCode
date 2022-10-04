#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import defaultdict



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        length = 0
        hashmap = {s[0]: 1}
        
        for R in range(1, len(s)):
            if s[R] in hashmap:
                hashmap[s[R]] += 1
            else:
                hashmap[s[R]] = 1

            while sum(hashmap.values()) - max(hashmap.values()) > k:
                hashmap[s[L]] -= 1
                L += 1
                
            length = max(length, R - L + 1)
            
        return length
        
# @lc code=end

