#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
import itertools
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for x, y in itertools.product(range(9), range(9)):
            cell_value = board[x][y]
            if cell_value == ".":
                continue
            if cell_value in rows[x] or cell_value in columns[y] or cell_value in squares[x//3][y//3]:
                return False

            rows[x].add(cell_value)
            columns[y].add(cell_value)
            squares[x//3][y//3].add(cell_value)

        return True
        
# @lc code=end

