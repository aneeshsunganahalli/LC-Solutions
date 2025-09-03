from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)


        # TLE
        # k = k % len(nums)
        # while k:
        #     last = nums[-1]
        #     for i in reversed(range(len(nums) - 1)):
        #         nums[i + 1] = nums[i]
        #     nums[0] = last
        #     k -= 1
        
                
        