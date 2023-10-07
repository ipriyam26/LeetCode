from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero,one,two=0,0,0
        
        for num in nums:
            if num==0:
                zero+=1
            elif num==1:
                one+=1
            else:
                two+=1
        
        nums = [0]*zero + [1]*one + [2]*two
        print(nums)

Solution().sortColors([2,0,2,1,1,0])