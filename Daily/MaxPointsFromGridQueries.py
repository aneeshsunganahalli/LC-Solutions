from typing import List
import heapq
# Approach: BFS + MinHeap

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

        rows, cols = len(grid), len(grid[0])

        q = [(n,i) for i,n in enumerate(queries)]
        q.sort()

        res = [0] * len(queries)
        minHeap = [(grid[0][0], 0, 0)]  # val, r , c
        points = 0
        visit = set([(0,0)])

        for limit, index in q:
            while minHeap and minHeap[0][0] < limit:
                val, r , c = heapq.heappop(minHeap)
                points += 1
                neighbours = [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]

                for nr, nc in neighbours:
                    if (
                        0 <= nr < rows and 0 <= nc < cols and 
                        (nr,nc) not in visit
                    ):
                        heapq.heappush(minHeap, (grid[nr][nc], nr, nc))
                        visit.add((nr,nc))
            res[index] = points
        return res