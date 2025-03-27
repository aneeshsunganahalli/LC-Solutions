from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        majority = 0
        count = 0

        for n in nums:  # Algo to find majority element in array
            if count == 0:
                majority = n
            if n == majority:
                count += 1
            else:
                count -= 1
        
        leftCount = 0
        rightCount = nums.count(majority) # Count of majority element

        for i in range(len(nums)):
            if nums[i] == majority:
                leftCount += 1
                rightCount -= 1
            
            leftLen = i + 1             # Just getting left and right subarray lengths
            rightLen = len(nums) - i - 1

            if 2 * leftCount > leftLen and 2 * rightCount > rightLen: # Main Condition if L + R = n, then L/2 + R/2 == n/2 which we want 
                return i
        return -1