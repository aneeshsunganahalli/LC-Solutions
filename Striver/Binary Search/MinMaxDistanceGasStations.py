"""
We have a horizontal number line. On that number line, we have gas stations at positions stations[0], stations[1], ..., stations[n-1]. Now, we add k more gas stations so that d, the maximum distance between adjacent gas stations, is minimized. We have to find the smallest possible value of d. Find the answer exactly to 2 decimal places.
Note: stations is in a strictly increasing order.

Examples:

Input: stations[] = [1, 2, 3, 4, 5], k = 2
Output: 1.00
Explanation: Since all gaps are already equal (1 unit each), adding extra stations in between does not reduce the maximum distance.
"""
class Solution:
    def minMaxDist(self, arr, k):
        
        def gasStationsRequired(mid):
            count = 0
            
            for i in range(1, len(arr)):
                numbersInBetween = (arr[i] - arr[i - 1]) / mid
                if arr[i] - arr[i - 1] == numbersInBetween * mid:
                    numbersInBetween -= 1
                count += numbersInBetween
            return count
        lo = 0
        hi = 0
        for i in range(len(arr) - 1):
            hi = max(hi, arr[i + 1] - arr[i])
        
        diff = 1e-3
        while hi - lo > diff:
            mid = (hi + lo) / 2.0
            count = gasStationsRequired(mid)
            if count > k:
                lo = mid
            else:
                hi = mid
        return hi