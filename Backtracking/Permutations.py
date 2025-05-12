from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        # Backtracking Solution
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums, pick: List[bool]):
        if len(perm) == len(nums):
            self.res.append(perm[:]) # Stores copy of full permutation in the res
            return
        
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)  # Does recursive call and makes current number as picked
                perm.pop()
                pick[i] = False

        
        # Easier Solution
        # Idea being start with 0 numbers and add one number at a time in any available position
        # if len(nums) == 0:
        #     return [[]]
        
        # perms = self.permute(nums[1:])
        # for p in perms:
        #     for i in range(len(p) + 1):
        #         p_copy = p.copy()
        #         p_copy.insert(i, nums[0])
        #         res.append(p_copy)
        # return res