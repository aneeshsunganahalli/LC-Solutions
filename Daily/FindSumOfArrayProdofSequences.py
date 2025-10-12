from typing import List
# 3539
class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        
        MOD = 10**9 + 7
        cache = {}

        def dfs(remPositions, remSetBits, index, carry):
            # Base Case: Invalid states
            # If we can't possibly achieve n set bits with remaining positions + carry
            if remPositions < 0 or remSetBits < 0 or remPositions + carry.bit_count() < remSetBits:
                return 0
            # Base Case: All positions filled
            if remPositions == 0:
                return 1 if remSetBits == carry.bit_count() else 0
            if index >= len(nums):
                return 0
            
            state = (remPositions, remSetBits, index, carry)
            if state in cache:
                return cache[state]
            
            res = 0
            # Decide t, nums[i] exactly t times (0 to r times)
            for t in range(remPositions + 1):
                # Binomial Coefficient: C(r, t) = ways to choose t positions from r
                w = 1
                for j in range(t):
                    w = w * (remPositions - j) // (j + 1)
                w %= MOD
                # Product Contribution: nums[i]^t (using t copies)
                v = pow(nums[index], t, MOD)

                nc = carry + t
                # - nc % 2: checks if current position has set bit after addition
                # - nc // 2: carry to next higher position
                # - We reduce n by 1 if current position becomes a set bit
                contribution = w * v % MOD * dfs(remPositions - t, remSetBits - (nc % 2), index + 1, nc // 2)
                res = (res + contribution) % MOD
            
            cache[state] = res
            return res
        
        return dfs(m, k, 0, 0)
