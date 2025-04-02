from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        # O(N^2)
        n = len(nums)
        res = 0
        left = nums[0]

        for j in range(1,n):
            if nums[j] > left:
                left = nums[j]
            for k in range(j + 1,n):
                res = max(res, (left - nums[j]) * nums[k])
        return res

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        # Brute Force O(N^3)
        n = len(nums)
        res = 0

        for i in range(n):
            for j in range(i + 1,n):
                for k in range(j + 1, n):
                    res = max(res, (nums[i] - nums[j]) * nums[k])
        return res