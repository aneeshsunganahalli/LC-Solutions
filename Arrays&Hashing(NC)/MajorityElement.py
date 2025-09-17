from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        # Moore's Voting Algo
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

        # My blind implementation of Moore's
        count = 1
        Element = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == Element:
                count += 1
            else:
                count -= 1
                if count == 0:
                    Element = nums[i]
                    count = 1
            i += 1
        return Element


        # PreSort
        if len(nums) == 1:
            return nums[0]

        bound = math.floor(len(nums) / 2)
        nums.sort()
        currLen = 1
        currVal = nums[0]
        i = 1
        while i < len(nums):
            if currVal == nums[i]:
                currLen += 1
                if currLen > bound:
                    return currVal
            else:
                currVal = nums[i]
                currLen = 1
            i += 1
