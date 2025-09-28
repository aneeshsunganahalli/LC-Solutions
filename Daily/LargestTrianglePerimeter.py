class Solution:
    def largestPerimeter(self, nums) -> int:
        
        nums.sort()
        
        if len(nums) >= 3:
            maxP = 0

            for i in range(len(nums) - 2):
                if nums[i] + nums[i  + 1] > nums[i + 2]:
                    maxP = max(maxP, nums[i] + nums[i + 1] + nums[i + 2])
            return maxP
        else:
            return 0