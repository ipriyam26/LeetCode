#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List


class Solution:
    def search_in_column(self,matrix: List[List[int]],target: int):
        start =0
        end = len(matrix)-1
        
        while start<=end:
            mid = start + (end-start)//2
            
            if matrix[mid][0]<target:
                start = mid+1
            elif matrix[mid][0]>target:
                end = mid-1
            else:
                return mid,True
        
        return end,False
    
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = start + (end - start)//2
            if nums[mid]<target:
                start=mid+1
            elif nums[mid]>target:
                end= mid-1
            else:
                return mid
        return -1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col,in_first = self.search_in_column(matrix=matrix,target=target)
        return True if in_first else self.search(nums=matrix[col],target=target) != -1

    
# if __name__ == "__main__":
#     print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,31,34,60]],15))

        
# @lc code=end

