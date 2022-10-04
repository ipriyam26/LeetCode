#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hashStore = {
            'a':0,
            'b':0,
            'c':0
        }
        result = 0
        i=0
        for j in range(len(s)):
            hashStore[s[j]]+=1
            while all(hashStore.values()):
                hashStore[s[i]]-=1
                i+=1
            result+=i
        return result
                
# @lc code=end

