from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

        # Tabulation
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

        # Memoization
        dp = [-1] * len(nums)
        
        def dfs(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(dfs(i + 1), dfs(i + 2) + nums[i])
            return dp[i]
        return dfs(0)
        
        # Recursion
        def dfs(i):
            if i >= len(nums):
                return 0
            return max(dfs(i + 1), dfs(i + 2) + nums[i])

        return dfs(0)