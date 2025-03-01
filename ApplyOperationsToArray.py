from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        left = 0
        for i in range(n):
            if nums[i] != 0: # Swap left and i pointer when u hit a non-zero after hitting a zero
                nums[i],nums[left] = nums[left],nums[i]
                left += 1
        return nums