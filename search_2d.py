from typing import List
from dataclasses import dataclass


class Solution:
    @dataclass
    class Response:
        is_final_result: bool
        value: int

    def find_relevant_row(self, target: int):
        low, high = 0, len(self.matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.matrix[mid][0] < target:
                low = mid + 1
            elif self.matrix[mid][0] > target:
                high = mid - 1
            else:
                return self.Response(True, mid)
        return self.Response(False, high)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.matrix = matrix
        response = self.find_relevant_row(target=target)
        if response.is_final_result:
            return True
        # print(response)
        row = self.matrix[response.value]

        low, high = 0, len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] < target:
                low = mid + 1
            elif row[mid] > target:
                high = mid - 1
            else:
                return True
        return False


matrix = [[1, 3, 5, 7, 9], [10, 11, 16, 20, 22], [23, 30, 34, 60, 61]]


def check(num: int):
    for row in matrix:
        for value in row:
            if value == num:
                return True
    return False


for i in range(1, 50):
    if Solution().searchMatrix(matrix=matrix, target=i) != check(i):
        print("Failed for ", i)
