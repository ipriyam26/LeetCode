from functools import lru_cache


class Solution:
    
    @lru_cache
    def recurr(self, row: int, column: int):
        if row == self.end_row and column == self.end_column:
            return 1
        total = 0
        if row == self.end_row:
            total += self.recurr(row=row, column=column + 1)
        elif column == self.end_column:
            total += self.recurr(row=row + 1, column=column)
        else:
            total += self.recurr(row=row + 1, column=column) + self.recurr(
                row=row, column=column + 1
            )
        return total
    def uniquePaths(self, m: int, n: int) -> int:
        self.end_row, self.end_column = m, n
        return self.recurr(1,1)

Solution().uniquePaths(3,7)