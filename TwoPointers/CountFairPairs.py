from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort() # Sort the array to use two pointers

        def find(m):
            n = len(nums)
            l, r = 0, n - 1
            count = 0
            while l < r:
                if nums[l] + nums[r] <= m:
                    count += r - l
                    l += 1       # Check if with next number valid pairs can be made
                else:
                    r -= 1
            return count
        
        return find(upper) - find(lower - 1)

        

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Brute Force
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                s = nums[i] + nums[j]
                if s >= lower and s <= upper:
                    res += 1
        return res