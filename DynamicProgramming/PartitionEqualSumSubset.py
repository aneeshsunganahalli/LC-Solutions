from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2:
            return False
        
        dp = set()  # Set to store all sums
        dp.add(0)
        target = sum(nums) // 2
        
        for i in range(len(nums) - 1, -1, -1):
            nextDp = set()  # Used to help update dp
            for t in dp:
                if t + nums[i] == target:
                    return True
                nextDp.add(t) # Add the current sum to nextDp
                nextDp.add(t + nums[i]) # Add the new sum to nextDp
            dp = nextDp

        return True if target in dp else False