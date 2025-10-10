from typing import List
# 1539
class Solution:
    def findKthPositive(self, arr, k):
        beg, end = 0, len(arr)
        while beg < end:
            mid = (beg + end) // 2
            if arr[mid] - mid - 1 < k:
                beg = mid + 1
            else:
                end = mid
        return end + k