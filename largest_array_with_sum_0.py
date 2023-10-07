from typing import Dict, List


class Solution:
    def maxLen(self, n:int, arr:List[int]):
        prefix_sum_arr = [arr[0]]
        prefix_sum_arr.extend(prefix_sum_arr[-1]+element for element in arr[1:])
        table:Dict[int,List[int]] = {0:[-1]}
        for i,prefix in enumerate(prefix_sum_arr):
            if prefix in table:
                table[prefix].append(i)
            else:
                table[prefix] = [i]
        max_len = 0
        max_arr = []

        for value in table.values():
            if value[-1] - value[0] > max_len:
                max_len = value[-1] - value[0]
                max_arr = arr[value[0]+1: value[-1]+1]
        return max_arr
                
            
            
            
Solution().maxLen(arr=[15,-2,2,-8,1,7,10,23],n=3)