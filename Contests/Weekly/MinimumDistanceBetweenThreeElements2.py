from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        hash = defaultdict(list)
        for i in range(len(nums)):
            hash[nums[i]].append(i)

        res = float('inf')
        for v in hash.values():
            if len(v) < 3:
                 continue
            for i in range(len(v) - 2):
                dist = abs(v[i] - v[i + 1]) + abs(v[i + 1] - v[i + 2]) + abs(v[i + 2] - v[i])
                if dist < res:
                    res = dist
        return res if res != float('inf') else -1