#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key=lambda x:(x[0],x[1]))
        low = intervals[0][0]
        high = intervals[0][1]
        result = []
        
        for i,j in intervals[1:]:
            
            if high <i:
                result.append([low,high])
                low=i
                high=j
            else:
                high =max(high,j)
        result.append([low,high])
        return result

# if __name__ == "__main__":
#     arr = [[1,3],[2,6],[8,10],[15,18]]
#     sol = Solution()
#     print(sol.merge(arr))
                
        
# @lc code=end

