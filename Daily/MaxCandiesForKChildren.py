from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        total = sum(candies)
        if total < k: # Can't give even 1 candy since there isn't enough
            return 0
        
        l = 1
        r = total // k # Max amount of candy that can be given to a child from given pile

        while l <= r: # Binary Search
            mid = (l + r) // 2
            piles = 0 # Keeps a track of how many piles in each iteration

            for c in candies:
                if c >= mid: # 
                    piles += c // mid # Calculates number of piles 
                    if piles >= k: break
            if piles >= k: # Found a number that can be given to all children
                res = mid  # So we look for a higher number, if any
                l = mid + 1
            else: # If we didn't find a number that can be given to all,
                r = mid - 1 # We look for a lower number to satisfy the condition
        return res