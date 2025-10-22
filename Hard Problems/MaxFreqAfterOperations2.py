from typing import List
from collections import defaultdict
# 3347
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:

        nums.sort()
        maxlen = 0
        l, r = 0, 0

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        for num in nums:
            while nums[l] < num - k:
                l += 1
            while r < len(nums) and nums[r] <= num + k:
                r += 1
            size = r - l  
            ops = size - freq[num]
            maxlen = max(maxlen, freq[num] + min(numOperations, ops))
        
        # For numbers not in array
        l = 0
        for r in range(len(nums)):
            while nums[l] < nums[r] - 2 * k:
                l += 1
            maxlen = max(maxlen, min(r - l + 1, numOperations))
        return maxlen
    