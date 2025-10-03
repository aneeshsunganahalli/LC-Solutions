from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if mid + 1 < len(nums) and nums[mid] < nums[mid + 1]:
                low = mid + 1
            elif mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                high = mid - 1
            else:
                return mid
            

        # Linear TC, Obvious Solution
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i  + 1]:
                return i
        
        if nums[0] > nums[1]:
            return 0
        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1