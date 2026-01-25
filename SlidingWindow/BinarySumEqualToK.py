# 930
from typing import List
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        count = defaultdict(int)
        count[0] = 1

        res = 0
        prefix = 0

        for n in nums:
            prefix += n 
            res += count[prefix - goal]
            count[prefix] += 1
        
        return res


        # Striver Solution
        def atmost(num):
            l = 0
            res = 0
            s = 0
            for r, n in enumerate(nums):
                s += n
                while l <= r and s > num:
                    s -= nums[l]
                    l += 1
                res += (r - l + 1)
            return res
        
        return atmost(goal) - atmost(goal - 1)