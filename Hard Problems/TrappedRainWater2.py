from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0 
        
        """
        Water trapped at a cell is limited by the minimum boundary height surrounding it.

        Process the outer boundary first and expand inward, always keeping track of the lowest boundary cell.

        Use a min-heap (priority queue) to always expand from the lowest effective boundary, simulating how water would naturally fill from the outside in.
        """

        visited = [[False]*n for _ in range(m)]
        heap = [] 

        
        for r in range(m):
            for c in (0, n-1):
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visited[r][c] = True
        for c in range(n):
            for r in (0, m-1):
                if not visited[r][c]:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        water = 0
        max_boundary = 0 
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        
        while heap:
            h, r, c = heapq.heappop(heap)
            
            if h > max_boundary:
                max_boundary = h

           
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    nh = heightMap[nr][nc]

                    
                    if nh < max_boundary:
                        water += max_boundary - nh


                    heapq.heappush(heap, (max(nh, max_boundary), nr, nc))

        return water
