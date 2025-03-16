from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def check(c: int):    # Function to check validity of the current mid
            i = 0
            count = 0

            while i < len(nums):
                if nums[i] <= c: # If its lesser, we will skip adjacent house
                    i += 2
                    count += 1
                else:             # Else we just move to next element
                    i += 1
                if count == k:
                    break
            return count == k
        
        l = 1
        r = max(nums)  # Result can only be between the min and max of the array
        res = 0

        while l <= r:
            mid = (l + r) // 2

            if check(mid): # If mid is valid, look for a lower number if any
                res = mid
                r = mid - 1
            else:           # If not valid, we need to check higher
                l = mid + 1
        return res
