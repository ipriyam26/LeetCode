from functools import lru_cache
from typing import List


class Solution:
    @lru_cache
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        current = []
        for i in range(numRows-1):
            for i in range(-1, len(pascal[-1]) + 1):
                if i in [-1, len(pascal[-1])]:
                    current.append(0)
                else:
                    current.append(pascal[-1][i] + pascal[-1][i + 1])
            pascal.append(current)
        return pascal
