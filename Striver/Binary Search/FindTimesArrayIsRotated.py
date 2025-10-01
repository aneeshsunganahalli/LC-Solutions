"""
Given an integer array nums of size n, sorted in ascending order with distinct values. The array has been right rotated an unknown number of times, between 0 and n-1 (including). Determine the number of rotations performed on the array.
"""

class Solution:
    def findKRotation(self, nums):

        low = 0
        high = len(nums) - 1
        res = 0

        """
        Idea is to find the index of the minimum value, to find minimum value 
        we have to check for where the array value suddenly decreases as the 
        min value is somewhere in the middle after the largest number and before
        the second smallest number.
        0 is between 7 and 1 here -> [4,5,6,7,0,1,2]
        """

        while low <= high:
            if nums[low] <= nums[high]:
                return low
            
            mid = (low + high) // 2
            nextIndex = (mid + 1) % len(nums)
            prevIndex = (mid - 1 + len(nums)) % len(nums)

            # Mid is minimum
            if nums[mid] <= nums[nextIndex] and nums[mid] <= nums[prevIndex]:
                return mid

            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        return res