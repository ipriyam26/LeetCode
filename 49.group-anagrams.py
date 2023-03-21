#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for word in strs:
            sr = tuple(sorted(word))
            if sr not in table:
                table[sr]=[word]
            else:
                table[sr].append(word)
        return list(table.values())

            
        
        
# @lc code=end

