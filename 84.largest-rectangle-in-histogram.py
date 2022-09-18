#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
from typing import List


class Solution:
    
    def find_NGR(self,arr:List[int])-> List[int]:
        stack = []
        res = []
        i =len(arr)-1
        while i>=0:
            if not stack:
                res.append(-1)
            elif (stack[-1] >arr[i]):
                res.append(stack[-1])
            else:
                while stack and stack[-1]<arr[i]:
                    stack.pop()
                if not stack:
                    res.append(-1)
                else:
                    res.append(stack[-1])
            stack.append(arr[i])
            i-=1
        res.reverse()
        return res
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        
# @lc code=end

