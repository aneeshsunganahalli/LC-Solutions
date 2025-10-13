"""
Given two sorted arrays a[] and b[] and an element k, the task is to find the element that would be at the kth position of the combined sorted array.

Examples :

Input: a[] = [2, 3, 6, 7, 9], b[] = [1, 4, 8, 10], k = 5
Output: 6
Explanation: The final combined sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.

Input: a[] = [1, 4, 8, 10, 12], b[] = [5, 7, 11, 15, 17], k = 6
Output: 10
Explanation: Combined sorted array is [1, 4, 5, 7, 8, 10, 11, 12, 15, 17]. The 6th element of this array is 10.
"""
class Solution:
    def kthElement(self, a, b, k):
        
        if len(a) > len(b):
            a, b = b, a
        
        lo = 0
        hi = len(a)
        
        while True:
            mid = (lo + hi) // 2
            j = k - mid
            
            # boundary guard
            if j < 0:
                hi = mid - 1
                continue
            if j > len(b):
                lo = mid + 1
                continue
            
            Aleft = a[mid - 1] if mid > 0 else float('-inf')
            Aright = a[mid] if mid < len(a) else float('inf')
            
            Bright = b[j] if j < len(b) else float('inf')
            Bleft = b[j - 1] if j > 0 else float('-inf')
            
            if Aleft <= Bright and Bleft <= Aright:
                return max(Aleft, Bleft)
            
            if Aleft > Bright:
                hi = mid - 1
            else:
                lo = mid + 1
                