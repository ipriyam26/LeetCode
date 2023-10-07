from typing import List


class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {num:i for i,num in enumerate(nums)}
        for i,num in enumerate(nums):
            look_up = target-num
            search = hash_map.get(look_up,-1)
            if search not in [-1, i]:
                return [i,search]
            
    