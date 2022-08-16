#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
from typing import Dict


class Solution:
    def isHappy(self, n: int) -> bool:
        fast = n
        slow= n
        f = 0
        while(f==0 or slow!=fast):
            f=1
            fast = self.sumOfSquare(self.sumOfSquare(fast))
            if fast==1:
                return True
            slow = self.sumOfSquare(slow)

        return False
    
    def sumOfSquare(self, n:int):
        return sum(int(i)**2 for i in str(n))
        
        
# @lc code=end

