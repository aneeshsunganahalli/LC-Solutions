from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Two Pointer Solution only needs O(1) extra space
        l = 0
        r = len(numbers) - 1

        current = numbers[l] + numbers[r]

        while current != target:
            if current > target:
                r -= 1
            else:
                l += 1
            current = numbers[l] + numbers[r]
        return [l + 1, r + 1]

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Hash Solution requires O(n) extra space
        hash = {}
        for i in range(len(numbers)):
            hash[numbers[i]] = i
        
        for i in range(len(numbers)):
            second = target - numbers[i]
            if second in hash and i != hash[second]:
                return [i + 1, hash[second] + 1]
        
