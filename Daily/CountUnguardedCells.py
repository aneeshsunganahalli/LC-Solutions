# 2257
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        grid = [[0] * n for _ in range(m)]
        # 0 = free, 1 = guard, 2 = wall, 3 = guardable

        for r,c in guards:
            grid[r][c] = 1
        for r,c in walls:
            grid[r][c] = 2

        def mark_guards(r,c):
            # Up
            for row in range(r + 1, m):
                if grid[row][c] in [1,2]:
                    break
                grid[row][c] = 3
            
            # Down
            for row in reversed(range(0, r)):
                if grid[row][c] in [1,2]:
                    break
                grid[row][c] = 3
            
            # Left
            for col in reversed(range(0, c)):
                if grid[r][col] in [1,2]:
                    break
                grid[r][col] = 3
            
            # Right
            for col in range(c + 1, n):
                if grid[r][col] in [1,2]:
                    break
                grid[r][col] = 3
            
        for r,c in guards:
            mark_guards(r,c)
        
        res = 0
        for row in grid:
            for num in row:
                if num == 0:
                    res += 1
        return res