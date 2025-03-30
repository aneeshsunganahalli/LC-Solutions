from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1
        res = nums[0] # First element is lowest in sorted cases

        while low <= high:
            if nums[low] < nums[high]: # Sorted Array
                res = min(res, nums[low])
                break
            
            mid = (low + high) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[low]: # Mid is part of left sorted array in this case, so we search right sorted array for the min
                low = mid + 1
            else:
                high = mid - 1
        return res