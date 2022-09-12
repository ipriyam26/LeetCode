#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        table = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif stack and table[stack[-1]] ==c :
                stack.pop()
            else:
                return False
        return not stack
        
        
# @lc code=end

