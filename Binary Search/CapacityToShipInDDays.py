from typing import List
# 1011
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        lo = max(weights)
        hi = sum(weights)
        res = hi

        def possible(capacity: int) -> bool:
            total = 0
            daysTaken = 1
            for w in weights:
                if total + w > capacity:
                    daysTaken += 1
                    if w > capacity:
                        return False
                    total = w
                else:
                    total += w
                
            if daysTaken <= days:
                return True
            return False

        while lo <= hi:
            mid = (lo + hi) // 2

            if possible(mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res
