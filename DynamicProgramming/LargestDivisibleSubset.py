from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Memoization Solution
        nums.sort
        cache = {}

        def backtrack(i):
            if len(nums) == i:
                return []
            if i in cache:
                return cache[i]
            
            res = [nums[i]]      
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + backtrack(j)
                    res = tmp if len(tmp) > len(res) else res
            cache[i] = res
            return res
        res = []
        for i in range(len(nums)):
            tmp = backtrack(i)
            res = tmp if len(tmp) > len(res) else res
        return res

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        # Tabulation
        nums.sort()
        dp = [[n] for n in nums]
        res = []
        for i in reversed(range(len(nums))):
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + dp[j]
                    dp[i] = tmp if len(tmp) > len(dp[i]) else dp[i]
            res = dp[i] if len(dp[i]) > len(res) else res
        return res