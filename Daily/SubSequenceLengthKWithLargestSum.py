from typing import List
from heapq import heappop, heappush, heapify
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        heap = [(-num,i) for i, num in enumerate(nums)]
        heapify(heap)
        valid = []

        while k:
            valid.append(heappop(heap))
            k -= 1
        
        valid.sort(key=lambda x: x[1])
        return [-num for num,_ in valid]
        