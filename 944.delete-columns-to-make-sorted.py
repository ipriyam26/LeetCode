#
# @lc app=leetcode id=944 lang=python3
#
# [944] Delete Columns to Make Sorted
#

# @lc code=start
from typing import List


class Solution:
    def minDeletionSize(self, A):
        return sum(any(a > b for a, b in zip(col, col[1:])) for col in zip(*A))
        
        
# @lc code=end

