from typing import List
from collections import deque

# Optimised Queue solution
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:

        q = deque() # Here you don't actually flip any bits, but you use a queue to track indices that have been flipped
        res = 0

        for i in range(len(nums)):
            while q and i > q[0] + k - 1: # To get rid of indices that won't affect current index
                q.popleft()
            
            if (nums[i] + len(q)) % 2 == 0: # Checks if a bit at an index is 0 after flips have occured
                if i + k > len(nums): # Can't make an array of all 1s
                    return -1
                res += 1
                q.append(i) # Add to queue as the element at this index has been flipped
        return res
    
# Sliding Window solution O(n * k), causes TLE

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        res = 0
        l = 0
        r = k - 1

        while r < n:
            if nums[l] == 0: # If 0, flip all bits in the window
                for i in range(l,r + 1): # Window is always between l and r
                    nums[i] = 1 - nums[i]
                res += 1
            l += 1
            r += 1
        if set(nums) == {1}: # Checks if entire array consists of 1
            return res
        return -1
