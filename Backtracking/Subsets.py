from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []    # Result with all subsets
        subset = [] # Tracks current subset

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())   # Once index reaches out of bounds, append copy of subset to res
                return
            
            subset.append(nums[i])  # Choosing to add a number to the subset
            backtrack(i + 1)    # Going Deeper in decision tree after picking number

            subset.pop()    # Choosing not to add current number
            backtrack(i + 1) # Goign deeper into tree without picking number
        
        backtrack(0) # Starts at index 0
        return res