from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums) - 2):
            if nums[i] == 0:           # If a bit is 0, you have to change that bit and next two (since 3 consecutive are asked)
                nums[i] = 1
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]
                res += 1
        if set(nums) == {1}:
            return res
        return -1