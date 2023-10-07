from typing import List


class Solution:
    def Nsum(
        self,
        nums: List[int],
        target: int,
        taken: List[int],
        taken_idx: List[int],
        N: int,
    ) -> List[int]:
        if N == 2:
            for i, num in enumerate(nums):
                look_up = target - num
                search = self.hash_map.get(look_up, -1)
                if search not in [-1, i]:
                    self.result.append(taken + [num, look_up])
                    break
            return
        else:
            for i, num in enumerate(nums):
                    self.Nsum(nums[i+1:] ,target - num, taken + [num], taken_idx + [i], N - 1)

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.hash_map = {num: i for i, num in enumerate(nums)}
        nums.sort()
        self.result = []
        self.Nsum(nums,target, [], [], 4)
        print(self.result)


arr = [1, 0, -1, 0, -2, 2]
Solution().fourSum(arr, 0)
