from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        diff = [0] * (N + 1)  # Difference Array
        s,pos = 0,0

        for i in range(N):
            while s + diff[i] < nums[i]:
                if pos == len(queries): # Checked all queries
                    return -1
                
                start,end,val = queries[pos]
                pos += 1

                if end < i: # Skipping useless queries
                    continue
                
                diff[max(i,start)] += val
                if end + 1 < N:
                    diff[end + 1] -= val

            s += diff[i]

        return pos
    
    ## Basic Idea
    # Skip Useless Queries
    # While sum + diff[i] < nums[i]
    # Keep applying range updates using queries
    # Once satisfied move to next element in array