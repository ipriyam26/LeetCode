#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        factor=1
        num = ""
        if s[0] == '+':
            s=s[1:]

        elif s[0] == '-':
            factor=-1
            s=s[1:]

        for letter in s:
            if not letter.isdigit():
                break
            num+=letter
        res = factor*int(num) if num else 0
        if res<-2**31:
            return -2**31
        elif res>2**31-1:
            return 2**31-1
        else:
            return res
                
                    
            
        
# @lc code=end

