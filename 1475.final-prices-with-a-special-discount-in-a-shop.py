#
# @lc app=leetcode id=1475 lang=python3
#
# [1475] Final Prices With a Special Discount in a Shop
#

# @lc code=start
from typing import List



class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        prices.reverse()
        stack = []
        result = []
        for price in prices:
            if not stack:
                result.append(0)
            elif stack[-1] < price:
                result.append(stack[-1])
            elif stack[-1] > price:
                while stack and stack[-1] > price:
                    stack.pop()
                if not stack:
                    result.append(0)
                else:
                    result.append(stack[-1])
            stack.append(price)
        result.reverse()
        print(result)
        return [(pri - res) for pri, res in zip(prices, result)]
            
        
# @lc code=end

