from typing import List
from collections import defaultdict

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        count = defaultdict(int)
        twice, missing = 0,0

        for i in range(N):
            for j in range(N):
                count[grid[i][j]] += 1
        
        for i in range(1, N**2 + 1):
            if count[i] == 2:
                twice = i
            if count[i] == 0:
                missing = i
        
        return [twice,missing]