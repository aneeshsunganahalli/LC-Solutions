from typing import List
# 3346
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:

        maxVal = max(nums) + k  + 1
        count = [0] * maxVal

        for num in nums:
            count[num] += 1
        
        for i in range(1, maxVal):
            count[i] += count[i - 1]
        
        res = 0
        for i in range(maxVal):
            left = max(0, i - k) # Lower Bound of element
            right = min(maxVal - 1, i + k) # Upper bound of element
            total = count[right] - (count[left - 1] if left else 0) # Total elements within range of i
            freq = count[i] - (count[i - 1] if i else 0)    # Elements already equal to i
            res = max(res, freq + min(numOperations, total - freq))
            # total - freq is how many elements you can change to nums[i] that isn't already equal to nums[i] but can only do this numOps number of times
        return res