from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums) # Use set for O(1) lookups
        res = 0

        for num in numSet:
            if num - 1 not in numSet: # Only start a sequence if previous number isnt in set
                length = 1
                while (num + length) in numSet:
                    length += 1
                res = max(res,length)
        return res