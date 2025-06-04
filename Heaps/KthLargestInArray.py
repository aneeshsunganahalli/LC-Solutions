from heapq import heappush, heappop
from typing import List
from heapq import heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]