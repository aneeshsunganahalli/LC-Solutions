from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l , r = 0, 0
        cur = 0             # BitMask, used to store what bits have been set
        res = 0             # Keeps track of window size

        for r in range(len(nums)):
            while cur & nums[r]:   # This loop makes sure that cur and nums are not overlapping by the end of it
                cur = cur ^ nums[l] # To undo & we use ^
                l += 1
            res = max(res, r - l + 1)
            cur = cur ^ nums[r]
        return res

# Idea is to use sliding window, and keep a cur variable to make sure succesive elements in binary don't overlap,
# Once they do overlap, remove elements at left pointer until they once again don't overlap