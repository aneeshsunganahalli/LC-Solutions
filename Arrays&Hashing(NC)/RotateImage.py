from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def reverse(row):
            l = 0
            r = len(row) - 1
            while l < r:
                row[l], row[r] = row[r], row[l]
                l += 1
                r -= 1

        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if r > c:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for row in matrix:
            reverse(row)
        
    