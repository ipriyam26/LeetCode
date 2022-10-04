#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
            d = defaultdict(int)
            d[0] = 1
            prefix = ans = 0
            for i in nums:
                prefix += i
                if(prefix - goal in d):
                    ans += d[prefix - goal]
                d[prefix] += 1
            return ans
    
                    
                
            
# @lc code=end

