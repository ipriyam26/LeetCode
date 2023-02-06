#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return
            if left < n:
                dfs(left + 1, right, f'{s}(')
            if right < left:
                dfs(left, right + 1, f'{s})')

        res = []
        dfs(0, 0, '')
        return res
        
# @lc code=end

