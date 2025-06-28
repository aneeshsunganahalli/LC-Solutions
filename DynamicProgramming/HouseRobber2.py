from typing import List
class Solution:
  def rob(self, nums: List[int]) -> int:

    # Tabulation
    if len(nums) == 1:
      return nums[0]
    return max(self.helper(nums[1:]),
               self.helper(nums[:-1]))
  
  def helper(self, nums: List[int]) -> int:
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
    cache = [[-1] * 2 for _ in range(len(nums))]
    def dfs(i,flag):
      if i >= len(nums) or (flag and i == len(nums) - 1):
        return 0
      if cache[i][flag] != -1:
        return cache[i][flag]
      
      cache[i][flag] = max(dfs(i + 1, flag), dfs(i + 2, flag or i == 0) + nums[i])
      return cache[i][flag]

    return max(dfs(0,True), dfs(0, False))



