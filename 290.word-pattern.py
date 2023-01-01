#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        store = {}
        words = s.split(" ")
        if len(pattern)!=len(words):
            return False
        unitl_now = set()
        for pat,word in zip(pattern,words):
            if (
                pat not in store
                and word in unitl_now
                or pat in store
                and store[pat] != word
            ):
                return False
            elif pat not in store:
                store[pat]=word
                unitl_now.add(word)
        return True
                    
        
# @lc code=end

