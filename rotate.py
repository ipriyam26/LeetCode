from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        finished = set()
        n = len(matrix)
        i, j = 0, 0
        while i < n:
            j = 0
            while j < n:
                if (i, j) in finished:
                    j += 1
                    continue
                original_i, original_j = i, j
                new_content = matrix[original_i][original_j]
                while True:
                    # old_i, old_j = i, j
                    i, j = j, abs(n - i - 1)
                    old_content = matrix[i][j]
                    matrix[i][j] = new_content
                    new_content = old_content
                    finished.add((i, j))
                    if i == original_i and j == original_j:
                        break
                j += 1
            i += 1
        # print(matrix)


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

# assert Solution().rotate(matrix=matrix) == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
