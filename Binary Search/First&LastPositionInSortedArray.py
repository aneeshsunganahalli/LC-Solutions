from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Cleaner Version (same complexity)
        def lowerBound(nums, low, high, target):
            while low <= high:
                mid = (low + high) >> 1
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low
        
        low = 0
        high = len(nums) - 1
        start = lowerBound(nums, low, high, target)
        end = lowerBound(nums, low, high, target + 1) - 1

        if start < len(nums) and nums[start] == target:
            return [start, end]
        return [-1, -1]
        
        # Initial 
        low = 0 
        high = len(nums) - 1
        start = -1
        end = -1
        exists = False

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                exists = True
                break
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1


        if exists:
            low = 0 
            high = len(nums) - 1     
            # Floor
            while low <= high:
                mid = (low + high) // 2

                if nums[mid] <= target:
                    start = mid
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1

            low = 0
            high = len(nums) - 1
            # Ceil
            while low <= high:
                mid =  (low + high) // 2

                if nums[mid] >= target:
                    end = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
            return [end, start]
        return [-1, -1]


                