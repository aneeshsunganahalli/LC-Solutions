from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        prefix = 0
        seen = defaultdict(int)
        seen[0] = 1
        for i in range(len(nums)):
            prefix += nums[i]
            remove = prefix - k
            res += seen[remove]
            seen[prefix] += 1
        return res