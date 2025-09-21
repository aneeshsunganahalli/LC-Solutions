from typing import List
import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        # Only two elements max can occur more than 33% of the time, so apply Voting Algo to find two highest values
        res = []
        count1, count2 = 0, 0
        v1, v2 = None, None

        for i in range(len(nums)):
            if count1 == 0 and nums[i] != v2:
                count1 = 1
                v1 = nums[i]
            elif count2 == 0 and nums[i] != v1:
                count2 = 1
                v2 = nums[i]
            elif nums[i] == v1:
                count1 += 1
            elif nums[i] == v2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
                
        # Validate if the two selected values satisfy the condition
        count1, count2 = 0, 0
        for num in nums:
            if num == v1:
                count1 += 1
            if num == v2:
                count2 += 1
        
        minimum = math.floor(len(nums) / 3)
        if count1 > minimum:
            res.append(v1)
        if count2 > minimum:
            res.append(v2)

        return res

        # Counter Solution, linear time but also linear space
        count = Counter(nums)
        enough = math.floor(len(nums) / 3)
        res = []

        for c in count.keys():
            if count[c] > enough:
                res.append(c)
        return res
