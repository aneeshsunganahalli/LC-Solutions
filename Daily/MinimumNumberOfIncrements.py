# 1526
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:

        res = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                res += target[i] - target[i - 1]
        return res 
