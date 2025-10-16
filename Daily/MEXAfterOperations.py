from typing import List
from collections import defaultdict
# 2598
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:

        freq = defaultdict(int)
        for i in range(len(nums)):
            rem = nums[i] % value
            freq[rem] += 1
        
        i = 0
        while True:
            if freq[i % value] == 0:
                return i
            freq[i % value] -= 1
            i += 1
