from typing import List
# 2300
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        n, m = len(spells), len(potions)
        pairs = [0] * n

        potions.sort()
        for s in range(n):
            lo, hi = 0, m - 1
            val = -1
            while lo <= hi:
                mid = (lo + hi) // 2

                if potions[mid] * spells[s] >= success:
                    val = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            pairs[s] = m - val if val != -1  else 0
        return pairs