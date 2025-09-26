from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        prefix = 1
        suffix = 1
        res = float('-inf')
        for i in range(len(nums)):
            if prefix == 0: prefix = 1  # For odd number of negative numbers, if we skip one of them,
            if suffix == 0: suffix = 1  # We get a prefix and suffix product, maximum of these is the result

            prefix *= nums[i]
            suffix *= nums[n - 1 - i]

            res = max(res, max(prefix, suffix))
        return res