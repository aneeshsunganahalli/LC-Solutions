from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        low = 0
        high = len(nums) - 1

        """
        Idea is based on the observation that pairs start off on even & odd indices before the single occuring number and after it they appear as odd & even indices, using that we can decide whether to go right or left of the current mid and result condition is that nums[mid - 1] != nums[mid] != nums[mid + 1], nums[mid] will be the unique result
        """

        while low <= high:
            mid = (low + high) // 2

            # Odd
            if mid % 2:
                if mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                    low = mid + 1
                elif mid +  1 < len(nums) and nums[mid] == nums[mid + 1]:
                    high = mid - 1
                else:
                    return nums[mid]
            # Even
            else:
                if mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                    high = mid - 1
                elif mid +  1 < len(nums) and nums[mid] == nums[mid + 1]:
                    low = mid + 1
                else:
                    return nums[mid]


            

    