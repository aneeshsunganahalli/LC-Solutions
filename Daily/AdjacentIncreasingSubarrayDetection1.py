from typing import List
# 3349
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def check(c):
            end = c + k - 1
            while c < end:
                if nums[c] >= nums[c + 1]:
                    return False
                c += 1
            return True

        n = len(nums)
        for a in range( n - 2 *k + 1):
            b = a + k
            if check(a) and check(b):
                return True
        return False
        