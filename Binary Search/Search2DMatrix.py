from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = (start + end) // 2

            if target in matrix[mid]:
                return True
            
            if target > matrix[mid][-1]:
                start = mid + 1
            else:
                end = mid - 1
        return False