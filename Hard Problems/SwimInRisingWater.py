from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        """
        Whether the swim is possible is a monotone function with respect to time, so we can binary search this function for the correct time: the smallest T for which the swim is possible.

        Say we guess that the correct time is T. To check whether it is possible, we perform a simple depth-first search where we can only walk in squares that are at most T.
        """
        rows = len(grid)
        cols = len(grid[0])

        def possible(mid: int):
            seen = set()

            def dfs(r,c):
                if r == rows - 1 and c == cols - 1:
                    return True
                
                seen.add((r,c))
                for dr, dc in [(0, -1), (-1, 0),(0,1),(1, 0)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen:
                        if grid[nr][nc] <= mid:
                            if dfs(nr, nc):
                                return True
                return False
            
            return grid[0][0] <= mid and dfs(0,0)

        def binarySearch():
            low, high = grid[0][0], max(max(row) for row in grid)

            while low < high:
                mid = (low + high) // 2
                if possible(mid):
                    high = mid
                else:
                    low = mid + 1
            return low
        
        return binarySearch()
        

