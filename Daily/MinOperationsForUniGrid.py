from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        nums = sorted(grid[i][j] for i in range(len(grid)) for j in range(len(grid[0])))  # Sort all elements

        middle = nums[len(nums) // 2] # Most Optimal to start at middle
        res = 0

        for num in nums:
            if abs(middle - num) % x == 0: 
                res += abs(middle - num) // x
            else:
                return -1
        return res