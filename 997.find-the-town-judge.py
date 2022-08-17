#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
from typing import List


class Solution:
    
            
    
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1 and not trust:
            return 1
        
        count = [0 for _ in range(n + 1)]
        count2 = [0 for _ in range(n + 1)]
        for relation in trust:
            count[relation[1]] += 1
            count2[relation[0]] += 1
        if n - 1 in count:
            suspect = count.index(n - 1)
            return suspect if count2[suspect] == 0 else -1
        else:
            return -1

        
# @lc code=end

