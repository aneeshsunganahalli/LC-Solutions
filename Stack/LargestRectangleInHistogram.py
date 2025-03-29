from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [] # Storing as (index, height) pairs
        maxArea = 0

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # If height being read is smaller, height at tos can't be extended, so its popped
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start,h))
        
        # Once all ones that cant be extended are popped out, there will be some bars left in the stack, for which we have to calculate possible areas for

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i)) # Using length of given array because we know we have reached the end of that array
        return maxArea