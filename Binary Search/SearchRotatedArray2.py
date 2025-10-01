from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True
            # Horrible edge cases like [1,0,1,1,1], if low, high and mid are equal, just ignore them and use the next indices
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1

            # Left Part is Sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right Part is Sorted
            if nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
