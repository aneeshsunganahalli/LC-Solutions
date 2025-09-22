from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if a > 0:  # Needs to be non-positive for sum of zero
                break
            if i > 0 and a == nums[i - 1]:  # Already processed
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                threeSum = nums[j] + nums[k] + a
                if threeSum < 0:
                    j += 1
                elif threeSum > 0:
                    k -= 1
                else:
                    res.append([a, nums[j], nums[k]])
                    j += 1
                    k -= 1 # To avoid duplicate, if we use same j,k we just get the same triplet later
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res

        # Quadratic
        ansSet = set()
        for i in range(len(nums)):
            tri = set()
            for j in range(i + 1, len(nums)):
                third = -(nums[i] + nums[j])
                if third in tri:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    ansSet.add(tuple(temp))
                tri.add(nums[j])

        return list(ansSet)

        # Brute Force (TLE)
        nums.sort()
        print(nums)
        a = 0
        res = set()

        while a < len(nums) - 2:
            b = a + 1
            while b < len(nums) - 1:
                c = b + 1
                while c < len(nums):
                    if nums[a] + nums[b] + nums[c] == 0:
                        res.add((nums[a], nums[b], nums[c]))
                    c += 1
                b += 1
            a += 1
        return list(res)
