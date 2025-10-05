# 1482
from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        n = len(bloomDay)
        if m * k > n:
            return -1
        
        low = 1
        high = max(bloomDay)
        res = 1
    
        while low <= high:

            mid = (low + high) // 2
            count = 0
            needed = 0
            for f in bloomDay:
                if f <= mid:
                    count += 1
                    if count == k:
                        needed += 1
                        count = 0
                else:
                    count = 0
            if needed >= m:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res