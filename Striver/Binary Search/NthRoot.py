"""
You are given 2 numbers n and m, the task is to find n√m (nth root of m). If the root is not integer then returns -1.
"""

class Solution:
    def nthRoot(self, n, m):
        
        if not m:
            return m
        
        l = 1
        h = m // n 
        
        while l <= h:
            mid = (l + h) // 2
            
            Nth_power = mid ** n
            if Nth_power == m:
                return mid
            elif Nth_power < m:
                l = mid + 1
            else:
                h = mid - 1
        
        return -1
       