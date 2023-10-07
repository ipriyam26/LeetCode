from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        breaking_point = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i+1]>nums[i]:
                breaking_point=i
                break
        if breaking_point==-1:
            nums.reverse()
            print(nums)
            return

        for i in range(len(nums) - 1, breaking_point, -1):
            if nums[i] > nums[breaking_point]:
                nums[i], nums[breaking_point] = nums[breaking_point], nums[i]
                break
        nums = nums[:breaking_point+1] + nums[breaking_point+1:][::-1]
        print(nums)
Solution().nextPermutation(nums=[1,3,2])