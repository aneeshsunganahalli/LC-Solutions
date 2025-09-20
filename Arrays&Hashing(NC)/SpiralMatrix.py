from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # Use four walls as boundaries and go in spiral order using a while loop
        
        rows = len(matrix)
        cols = len(matrix[0])

        up = 0
        down = rows - 1
        left = 0 
        right = cols - 1

        res = []

        while up <= down and left <= right:
            for c in range(left, right + 1):
                res.append(matrix[up][c])
            up += 1
            if up > down: break

            for r in range(up, down + 1):
                res.append(matrix[r][right])
            right -= 1
            if right < left: break

            for c in range(right, left - 1, -1):
                res.append(matrix[down][c])
            down -= 1

            for r in range(down, up - 1, -1):
                res.append(matrix[r][left])
            left += 1
        
        return res