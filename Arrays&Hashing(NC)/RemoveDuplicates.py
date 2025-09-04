from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        curr = nums[0]
        pos = 1

        for i in range(1,n):
            if nums[i] != curr:
                curr = nums[i]
                nums[pos] = curr
                pos += 1
        return pos