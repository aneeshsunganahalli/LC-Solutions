from typing import List
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        
        z1 = nums1.count(0)
        z2 = nums2.count(0)
        s1, s2 = sum(nums1), sum(nums2)

        if not z1 and not z2:
            return s1 if s1 == s2 else -1
        if z1 and not z2:
            return s2 if s1 + z1 <= s2 else -1
        if not z1 and z2:
            return s1 if s2 + z2 <= s1 else -1
        
        return max(s1 + z1, s2 + z2)



        # Doesn't work, 616/636 cases
        # def zeroCount(num: List[int]):
        #     count = 0
        #     for n in num:
        #         if n == 0:
        #             count += 1
        #     return count
        
        # if len(nums1) < len(nums2):
        #     nums1, nums2 = nums2, nums1
        
        # z1 = zeroCount(nums1)
        # z2 = zeroCount(nums2)

        # if z2 == 0:
        #     return -1
        # else:
        #     c = nums1 if sum(nums1) > sum(nums2) else nums2
        #     return sum(c) + zeroCount(c)
