from typing import List
# 1901
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        m, n = len(mat), len(mat[0])

        # Find the max of a particular column along with row index
        def findColMax(col):
            largest = -1
            row = -1
            for i in range(m):
                if mat[i][col] > largest:
                    largest = mat[i][col]
                    row = i
            return row, largest
        
        lo, hi = 0, n - 1 # Binary Search on Columns
        while lo < hi:
            mid = (lo + hi) // 2
            row, val = findColMax(mid)
            rightVal = mat[row][mid + 1] # Value to the right of mid

            if val < rightVal:
                lo = mid + 1 # We want the larger element
            else:
                hi = mid
            
        return [findColMax(lo)[0], lo]

        
