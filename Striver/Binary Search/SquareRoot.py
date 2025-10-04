"""
Given a positive integer n, find the square root of n. If n is not a perfect square, then return the floor value.
"""
class Solution:
    def floorSqrt(self, n): 
        
        
        low = 1
        high = n // 2
        res = 1
        
        while low <= high:
            mid = (low + high) // 2
            
            square = mid**2
            
            if square <= n:
                low = mid + 1
                res = mid
            else:
                high = mid - 1
            
        return res