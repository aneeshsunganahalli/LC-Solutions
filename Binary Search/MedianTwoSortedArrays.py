from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2 # Easier naming
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B): # We want A to always be smallest
            A, B = B, A
        
        l, r = 0, len(A) - 1
        
        while True:
            mid = (l + r) // 2
            j = half - mid - 2 # Pointer to mark end of left partition of bigger array

            # Boundary elements of both arrays when partition is taken for current mid value
            Aleft = A[mid] if mid >= 0 else float("-inf")
            Aright = A[mid + 1] if mid + 1 < len(A) else float("inf")

            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            if Bleft <= Aright and Aleft <= Bright:   # Condition for valid partition
                if total % 2:   # Odd number of elements
                    return min(Bright, Aright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = mid - 1 # Need to increase larger area left partition
            else:
                l = mid + 1