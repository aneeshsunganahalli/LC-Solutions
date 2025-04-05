from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def backtrack(i, total):
            if i == len(nums):
                return total
            
            include = backtrack(i + 1, total ^ nums[i]) # Includes nums[i]
            exclude = backtrack(i + 1, total)   # Excludes nums[i] from the total

            return include + exclude    
        return backtrack(0,0)