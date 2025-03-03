from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        count = 0
        res1,res2 = [], []

        for num in nums:
            if num == pivot:
                count += 1
            elif num < pivot:
                res1.append(num)
            else:
                res2.append(num)
        return res1 + [pivot]*count + res2