from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        # Think of array as a number, and you wanna find out the next largest number
        # Check for the longest prefix, for which you can create bigger number from rearranging the rest of the elements.
        # To do this check from the back, for nums[i] < nums[i + 1], to get this breaking point
        # Edge case: if no breaking point, reverse for answer
        # Find smallest number larger than breaking point and swap
        # Reverse the array right of the breaking point

        def reverse(nums, beg, end):
            while beg < end:
                nums[beg], nums[end] = nums[end], nums[beg]
                beg += 1
                end -= 1

        idx = -1
        i = len(nums) - 2

        while i >= 0:
            if nums[i] < nums[i + 1]:
                idx = i
                break
            i -= 1

        if idx == -1:
            reverse(nums, 0, len(nums) - 1)

        else:
            j = len(nums) - 1
            while j > idx:
                if nums[j] > nums[idx]:
                    nums[j], nums[idx] = nums[idx], nums[j]
                    break
                j -= 1
            reverse(nums, idx + 1, len(nums) - 1)
                
        
