from typing import List
import math
# 1283
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        lo = 1
        hi = max(nums)
        res = 1
        while lo <= hi:
            mid = (lo + hi) // 2
            total = 0
            for num in nums:
                val = math.ceil(num / mid)
                total += val
            if total <= threshold:
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res
