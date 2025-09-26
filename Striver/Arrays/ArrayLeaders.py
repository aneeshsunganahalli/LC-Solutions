class Solution:
    def leaders(self, nums):
        
        i = len(nums) - 2
        res = []
        
        res.append(nums[-1])
        maxElement = nums[-1]
        
        while i >= 0:
            if nums[i] >= maxElement:
                maxElement = nums[i]
                res.append(nums[i])
            i -= 1
        
        def reverse(nums):
            i = 0
            j = len(nums) - 1
            
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        reverse(res)
        return res