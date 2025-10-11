# 410
from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def possible(mid):
            sub = 1
            total = 0
            for i in range(len(nums)):
                if total + nums[i] > mid:
                    sub += 1
                    total = nums[i]
                    if sub > k:
                        return False
                else:
                    total += nums[i]
            return True

        lo = max(nums)
        hi = sum(nums)
        res = hi

        while lo <= hi:
            mid = (lo + hi) // 2
            if possible(mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res