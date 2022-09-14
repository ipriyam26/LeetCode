#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        return self.find_NGR(nums)
    
    def find_NGR(self,arr:List[int])-> List[int]:
        copy = arr.copy()
        copy.reverse()
        stack = copy
        res = []
        i =len(arr)-1
        while i>=0:
            if not stack:
                res.append(-1)
            elif (stack[-1] >arr[i]):
                res.append(stack[-1])
            else:
                while stack and stack[-1]<=arr[i]:
                    stack.pop()
                if not stack:
                    res.append(-1)
                else:
                    res.append(stack[-1])
            stack.append(arr[i])
            i-=1
        res.reverse()
        return res
        
# @lc code=end

