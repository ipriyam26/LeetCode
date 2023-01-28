#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        num_to_letter = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        results = list(num_to_letter[int(digits[0])])
        for digit in digits[1:]:
            results =[element+l for l in num_to_letter[int(digit)] for element in results]
        return results
            

# if __name__ == "__main__":
#     print(Solution().letterCombinations("23"))
# @lc code=end
