from typing import List
from collections import Counter

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        distinct = len(set(nums))
        complete = 0
        count = Counter()
        i = 0
        for j in range(len(nums)):
            count[nums[j]] += 1
            while len(count) == distinct:
                count[nums[i]] -= 1
                if count[nums[i]] == 0:
                    del count[nums[i]]
                i += 1
            complete += i
        return complete

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        distinct = set(nums)    
        k = len(distinct)

        l = 0
        r = k - 1
        count = 0

        while r < len(nums):
            while len(set(nums[l:r+1])) == k:
                count += len(nums) - r
                l += 1
            r += 1
        return count