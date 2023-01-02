#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        table = Counter(s).most_common()
        table.sort(key=lambda item:(-item[1],item[0]))
        return "".join(element*count for element, count in table)
        
        
# @lc code=end

