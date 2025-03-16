from typing import List
from math import sqrt

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

    
        time = ranks[0] * cars ** 2

        l = 1
        r = time
        res = -1

        def count(m):
            total = 0
            for r in ranks:
                total += int(sqrt(mid/r))
            return total

        while l <= r:
            mid = (l + r) // 2
            
            repaired = count(mid)

            if repaired >= cars:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res