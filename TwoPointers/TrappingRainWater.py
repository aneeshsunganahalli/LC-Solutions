from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        res = 0

        if not height: return 0

        leftMax = height[l] # Used to store current left most max
        rightMax = height[r] # Used to store current right most max

        while l < r:
            if leftMax < rightMax: # We want the minimum of these to subtarct from current height
                l += 1          # Increase l pointer and check if a new left max is found and then subtract
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l] # Will be positive no matter what
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res # Will have kept track of all water trapped