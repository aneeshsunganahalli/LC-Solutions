from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        Sum,maxSum,minSum = 0,0,0

        for i in nums:
            Sum += i
            if Sum > maxSum:
                maxSum = Sum
            if Sum < minSum:
                minSum = Sum

        return abs(maxSum - minSum)
    
"""
Less optimal first solution, applying Kadanes algo twice to find Max sum and Min sum and then comparing

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxSum = nums[0]
        minSum = nums[0]
        curSum = nums[0]
        curMin = nums[0]

        for i in range(1,len(nums)):
            maxSum = max(nums[i], maxSum + nums[i])
            curSum = max(maxSum,curSum)
            minSum = min(nums[i], minSum + nums[i])
            curMin = min(curMin,minSum)

        return max(curSum,abs(curMin))
"""