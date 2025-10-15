from typing import List
# 3350
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev = 0
        res = 0
        N = len(nums)
        i = 0
        def check(i):
            count = 1
            while i + 1 < N and nums[i] < nums[i + 1]:
                i += 1
                count += 1
            return count
        while i < N:
            curr = check(i)
            res = max(res, min(prev, curr))
            res = max(res, curr // 2)
            prev = curr
            i += curr
        return res