from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res = []

        for a, m in enumerate(nums):
            if a > 0 and m == nums[a - 1]:
                continue
            
            for b, n in enumerate(nums[a+1:], start=a+1):
                if b > a + 1 and n == nums[b - 1]:
                    continue

                c = b + 1
                d = len(nums) - 1
                while c < d:
                    val = n + m + nums[c] + nums[d] - target
                    if val < 0:
                        c += 1
                    elif val > 0:
                        d -= 1
                    else:
                        res.append([n,m,nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while nums[c] == nums[c - 1] and c < d:
                            c += 1
        return res