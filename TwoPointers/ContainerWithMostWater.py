from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Two Pointer O(N)
        res = 0
        l , r = 0, len(height) - 1

        while l < r:
            length = r - l
            area = min(height[l], height[r]) * length
            
            if area > res:
                res = area
                
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute Force
        res = 0

        for i in range(len(height)):
            for j in range(i,len(height)):
                area = min(height[i], height[j]) * (j - i)
                res = max(area, res)
        return res