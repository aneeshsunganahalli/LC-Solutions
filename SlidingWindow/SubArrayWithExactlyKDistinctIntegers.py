# 992
from typing import List
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        

        # Applying Exact(k) = Atmost(k) - Atmost(k - 1)

        def atmost(num):
            l, res = 0,0
            count = {}

            for r, n in enumerate(nums):
                count[nums[r]] = count.get(nums[r], 0) + 1

                while l <= r and len(count) > num:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l += 1
                
                res += (r - l + 1)
            return res
        
        exact = atmost(k) - atmost(k - 1)
        return exact