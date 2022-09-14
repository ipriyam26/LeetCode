#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    
    def find_str(self, s):
        s1 = []
        for letter in s:
            if not s1 and letter != '#' or s1 and letter != '#':
                s1.append(letter)
            elif s1:
                s1.pop()
        return s1
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = self.find_str(s)
        t1 = self.find_str(t)
        print(s1,t1)
        return s1==t1
        
        
            
        
# @lc code=end

