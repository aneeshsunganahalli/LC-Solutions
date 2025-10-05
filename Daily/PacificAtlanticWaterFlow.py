from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
 
        rows = len(heights)
        cols = len(heights[0])
        res = []
        # Approach: See which cells reach pacific and atlantic ocean seperately and result is the intersection
        # We apply dfs from the oceans inward to land, to see from which cells water can flow from
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        def dfs(r, c, visited):
            visited[r][c] = True

            for dr, dc in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                
                """
                Conditions to check neighbour:
                    - neighbour is in grid
                    - neighbour is NOT visited
                    - Height of neighbour must be higher or equal than current height so water flows, since
                    we are checking from the ocean 
                """
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        # Pacific borders the top-most row and left-most column &
        # Atlantic borders the bottom row and right-most column
        
        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols - 1, atlantic)

        for j in range(cols):
            dfs(0, j, pacific)
            dfs(rows - 1, j, atlantic)

        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res           
        

        

            
