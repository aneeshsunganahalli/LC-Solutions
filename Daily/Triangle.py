from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        # No Extra Space
        # Start from second last row, add min of two adj elements of next row to each element of current row
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(
                    triangle[i + 1][j],
                    triangle[i + 1][j + 1]
                )

        return triangle[0][0]

        # Initial Recursive Solution
        cache = {}
        def dfs(row, col):
            if col > row or row >= len(triangle):   
                return 0
            
            if (row,col) in cache:
                return cache[(row,col)]
            
            cache[(row,col)] = min(
                triangle[row][col] + dfs(row + 1, col),
                triangle[row][col] + dfs(row + 1, col + 1)
            )
            return cache[(row,col)]

        return dfs(0,0)
