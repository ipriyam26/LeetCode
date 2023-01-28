#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        MAX_NEG = -2**31
        MAX_POS = 2**31 -1
        is_negative = x < 0
        num = str(x)
        if is_negative:
            num = num[1:]
        back_to_int = int(num[::-1])
        if back_to_int<MAX_NEG or back_to_int>MAX_POS:
            back_to_int=0
        if is_negative:
            back_to_int*=-1
        return back_to_int
        
# @lc code=end

