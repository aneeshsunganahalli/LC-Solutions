from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Approach is start from last index and keep putting the largest element
        lastIndex = m + n - 1
        i = m - 1
        j = n - 1

        # While loop condition is j >= 0 because if j reaches 0 before i that just means
        # all the larger elements were in nums2 and nums1 elements will stay in same position
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[lastIndex] = nums1[i]
                i -= 1
            else:
                nums1[lastIndex] = nums2[j]
                j -= 1
            lastIndex -= 1

