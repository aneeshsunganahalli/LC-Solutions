from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            
            if nums[mid] >= nums[l]:  # Mid and L are in left sorted array
                if target > nums[mid] or target < nums[l]: # We need to go right
                    l = mid + 1
                else:
                    r = mid - 1
            else: # Mid and R are in right sorted array
                if target < nums[mid] or target > nums[r]: # We need to go left
                    r = mid - 1
                else:
                    l = mid + 1
        return -1