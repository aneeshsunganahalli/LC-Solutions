from typing import List
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        nums.sort() # Sorting
        MOD = 10**9 + 7
        res = 0

        power = [1] * len(nums)
        for i in range(1, len(nums)):
            power[i] = (power[i - 1] * 2) % MOD
        
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] <= target:
                res = (res + power[r - l]) % MOD
                l += 1
            else:
                r -= 1
        return res

            
        
        