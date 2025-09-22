from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)
        pos = 0
        neg = 1

        for i in range(len(nums)):
            if nums[i] > 0:
                res[pos] = nums[i]
                pos += 2
            else:
                res[neg] = nums[i]
                neg += 2
        return res
    

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        # Brute Solution
        pos = []
        neg = []
        
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        res = []
        i = 0
        while i < len(pos):
            res.append(pos[i])
            res.append(neg[i])
            i += 1
        
        return res