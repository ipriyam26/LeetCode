#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
from typing import List


class MedianFinder:

    def __init__(self):
        self.is_odd = None
        self.values = []
        self.median_index = 0
    
    def _find_right_place_to_insert(self,nums:List[int],num:int)  :
        high = len(nums)-1
        low = 0
        while low<=high:
            mid = (low+high)//2
            if(nums[mid]>num):
                high = mid-1
            elif(nums[mid]<num):
                low = mid+1
            else:
                return mid
        return high-1
    
                

    def addNum(self, num: int) -> None:
        
        

    def findMedian(self) -> float:
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

