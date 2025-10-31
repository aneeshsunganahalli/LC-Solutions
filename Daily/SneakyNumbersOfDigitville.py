# 3289
from typing import List
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        # Mark occurrences by adding n at index = nums[i] % n
        for i in range(n):
            idx = nums[i] % n
            nums[idx] += n

        # Any index i where nums[i] // n == 2 means number i appeared twice
        for i in range(n):
            if nums[i] // n == 2:
                res.append(i)
                if len(res) == 2:
                    break  # only two sneaky numbers exist

        return res

        # Trivial Solution
        seen = set()
        res = []
        for num in nums:
            if num in seen:
                res.append(num)
            else:
                seen.add(num)
        return res