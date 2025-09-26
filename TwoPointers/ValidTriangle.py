from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums.sort()
        count = 0

        # when nums[first] + nums[second] > third, then every index in [first, first+1, ..., second-1] paired with second also forms a valid pair, so second - first valid triangles are added — then you must decrement second to continue checking other second values for the same third.

        i = len(nums) - 1
        while i >= 2:
            third = nums[i]
            first = 0
            second = i - 1

            while first < second:
                if nums[first] + nums[second] > third:
                    count += second - first
                    second -= 1
                else:
                    first += 1
            i -= 1
        return count
