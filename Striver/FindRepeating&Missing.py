"""
Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, and another number occurs twice in the array, find both the duplicate number and the missing number.
"""

from collections import defaultdict

class Solution:
    def findTwoElement(self, nums):
        
        n = len(nums)
        
        Sn = (n * (n + 1) // 2) # Sum of n numbers
        S2n = (n * (n + 1) * (2 * n + 1)) // 6 # Sum of squares
        
        S = 0   # Sum of array
        S2 = 0 # Sum of squares of array elements
        
        for i in range(n):
            S += nums[i]
            S2 += nums[i]**2
            
        # X -> repeated number
        # Y -> missing number
        
        XminusY = S - Sn
        squareDiff = S2 - S2n
        
        XplusY = squareDiff // XminusY
        
        X = (XplusY + XminusY) // 2
        
        Y = XplusY - X
        
        return [X,Y]
        
        # Initial solution using extra space
        seen = defaultdict(int)
        missing = 0
        repeated = 0
        n = len(nums)
        
        for i in range(len(nums)):
            if nums[i] in seen:
                repeated = nums[i]
            else:
                seen[nums[i]] = 1
        
        actual = sum(nums) - repeated
        expected = (n * (n + 1)) // 2
        
        missing = expected - actual
        
        return [repeated, missing]