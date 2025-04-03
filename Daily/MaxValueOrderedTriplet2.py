from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        n = len(nums)
        maxElement = nums[0]
        maxDiff = 0
        maxTriplet = 0
        for i in range(n):
            maxTriplet = max(maxTriplet, maxDiff * nums[i]) # Checking for max triplet before updating new max

            maxElement = max(maxElement, nums[i])   # Gets you max element to start triplet with
            maxDiff = max(maxDiff, maxElement - nums[i]) # Gets you greatest difference
            
        return maxTriplet
    