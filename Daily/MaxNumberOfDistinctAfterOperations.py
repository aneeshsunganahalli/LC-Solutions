from typing import List
# 3397
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        before = float('-inf')
        distinct = 0

        for num in nums:
            lower_bound = num - k
            upper_bound = num + k

            if before < lower_bound:
                before = lower_bound
            else:
                before += 1
            
            if before <= upper_bound:
                distinct += 1
            else:
                before -= 1
        return distinct