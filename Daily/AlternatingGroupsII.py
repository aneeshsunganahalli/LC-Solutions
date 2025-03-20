from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors)
        l = 0
        groups = 0

        for r in range(1,N + k - 1):
            if colors[r % N] == colors[(r-1) % N]: # Check for Non Alternating Pair
                l = r
            
            if r - l + 1 > k:
                l += 1
            if r - l + 1 == k:
                groups += 1
        
        return groups
