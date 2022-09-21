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
        if not self.values:
            self.values.append(num)
            self.is_odd = True
            return
        i = self._find_right_place_to_insert(self.values,num)
        self.is_odd = not self.is_odd
        self.values.insert(i,num)
        
        
        
        

    def findMedian(self) -> float:
        mid = len(self.values)//2+1
        if self.is_odd:
            print(self.values[mid])
            return self.values[mid]
        mid_1 = mid-1
        print(mid,mid_1)
        vv = (self.values[mid]+self.values[mid_1])/2
        print(vv)
        return vv
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

