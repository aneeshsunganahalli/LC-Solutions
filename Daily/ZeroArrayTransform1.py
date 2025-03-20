from typing import List 


# Brute Force leads to TLE
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        temp =  nums

        for i in range(len(queries)):
            l = queries[i][0]
            r = queries[i][1]

            while l <=  r:
                if temp[l] > 0:
                    temp[l] -= 1
                l += 1
            
        if set(temp) == {0}:
            return True
        return False

# Improved Solution using Line Sweep
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        line = [0] * (len(nums) + 1)

        for start, end in queries: # Add 1 for every starting index, and -1 for every ending at the end+1 index
            line[start] += 1
            line[end + 1] -= 1
        
        for i in range(1,len(line)): # Each element of line sweep is made to be sum of all previous
            line[i] += line[i-1]
        
        for i in range(len(nums)): # If number at index i in nums is larger than in line, that element cant be zero at the end
            if line[i] < nums[i]:
                return False
        return True