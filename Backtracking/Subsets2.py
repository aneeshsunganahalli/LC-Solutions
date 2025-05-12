from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()     # Usually to remove duplicates, we sort first
        res = []

        def backtrack(i, subset):
            if i == len(nums):  # Terminating Base
                res.append(subset[:])
                return
            
            subset.append(nums[i])  # Choose number
            backtrack(i + 1, subset)    # Recursive call after including
            subset.pop()    # Skip the number
            
            while i + 1 < len(nums) and nums[i] == nums[i+1]:   # Getting rid of duplicates
                i += 1
            backtrack(i + 1, subset)    # Now do recurisve call to avoid duplicare subsets
        backtrack(0, [])    # Main func call
        return res