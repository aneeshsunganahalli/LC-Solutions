from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        currSum = 0
        maxSum = float('-inf')
        
        # Works on the concept of when subarray gives u a negative sum, reset sum back to 0
        for r in range(len(nums)):
            if currSum < 0:
                currSum = 0
            currSum += nums[r]
            maxSum = max(currSum, maxSum)
        return maxSum