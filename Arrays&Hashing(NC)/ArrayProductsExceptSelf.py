from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: # Use prefix product and suffix product

        n = len(nums)
        res = [0] * n
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = suffix[n-1] = 1

        for i in range(1,n):
            prefix[i] = prefix[i - 1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        

        return res
    
  

# More Optimal

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        for i in range(1,n):
            result[i] *= result[i-1] * nums[i-1]
        
        suffix = 1

        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
       
            