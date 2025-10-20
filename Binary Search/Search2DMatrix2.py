from typing import List
# 240
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Optimal Staircase Solution
        m = len(matrix)
        n = len(matrix[0])
        r, c = 0, n - 1

        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False

        # Initial M logN Solution
        for row in matrix:
            lo = 0 
            hi = len(row) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if target == row[mid]:
                    return True
                elif target > row[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False