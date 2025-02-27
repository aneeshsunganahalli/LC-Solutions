from typing import List

# Brute Force O(N^2 Log N)ish, checking for all possible pairs
class Solution:
    def lenLongestFibSubseq(self, nums: List[int]) -> int:
        
        arr = set(nums)
        res = 0
        
        for i in range(len(nums) - 1):
            for j in range(i+1,len(nums)):
                prev = nums[i]
                curr = nums[j]
                nxt = prev + curr
                length = 2
                
                while nxt in arr:
                    prev = curr
                    curr = nxt
                    nxt = prev + curr
                    length += 1

                    res = max(res,length)
        return res