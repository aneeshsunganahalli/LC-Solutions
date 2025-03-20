from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        l , r = 0, len(nums) - 1

        while l <= r:   # To find 0 basically
            mid = (l + r) // 2
            if nums[mid] <= 0:
                l = mid + 1
            else:
                r = mid - 1
        
        pos = len(nums) - l

        l -= 1      # To bring back l to point to 0 if any
        while l >= 0 and nums[l] == 0: # To eliminate remaning zeroes
            l -= 1
        
        neg = l + 1

        return max(pos,neg)